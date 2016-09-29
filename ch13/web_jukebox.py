'''
JukeBox 웹 인터페이스
=====================

- Jukebox를 제어할 웹서비스

기능:
  - pages:
    - /           : 메인 페이지
    - /player     : jukebox의 현재 곡 표시, 다음곡, 중지, 다시 실행 기능
    - /library    : jukebox의 DB에 등록되어 있는 곡 리스트
    - /add_song   : 새로운 곡 추가

  - ajax api:
    - GET  /jukebox/current_song  : 현재 플레이 되고 있는 정보
    - POST /jukebox/songs         : 새로운 곡 추가
    - POST /jukebox/playlist      : DB에 있는 곡을 플레이 리스트에 추가
    - POST /jukebox/control/<cmd> : 재생, 중지, 다음곡 명령 수행
      - cmd
         - play
         - stop
         - next

  - filter
    - duration_time     : 곡 길이를 시:분:초 로 표시

'''

import os, sys
import youtube
from flask import Flask, request, render_template, make_response, jsonify
from song import Song

__author__ = 'jinsub ahn <jinniahn@gmail.com>'

# Flask 객체 하나 생성
# css, js, img들을 담을 폴더를 지정한다.(web/static)
# jinja 템플릿으로 사용할 폴더 위치 (web/web-doc)
app = Flask(__name__
            , static_folder='web/static'
            , template_folder='web/web-doc')
import json

# Jukebox 클래스
from jukebox import JukeBox, AddYoutubeListThread

# jukebox 제어용 객체 생성
# 주로 Web 인터페이스에서 받는 명령을 jukebox 객체에서 처리한다.
jukebox = JukeBox()

#--------------------
# Pages
#--------------------
@app.route('/')
def main():
    # web/web-doc/main.html를 렌더링해서 반환한다.
    return render_template("main.html")

@app.route('/player')
def player():
    # 현재 플레이 되고 있는 노래
    current_song = jukebox.current_song()
    # 현재 가지고 있는 playlist 목록
    playlist     = jukebox.current_playlist()

    # 웹 페이지로 만들어 전달
    return render_template("player.html"
                           , current_song = current_song and current_song.to_dict() or {}
                           , playlist = playlist )

@app.route('/library')
def library():
    # DB에 있는 노래 목록
    songs = jukebox.get_db_songs()
    return render_template("library.html"
                           , songs = songs)

@app.route('/add_song')
def songs():
    return render_template("add_song.html")

#--------------------
# AJAX용 API
#--------------------

@app.route('/jukebox/current_song', methods=['GET'])
def get_current_song():
    "현재 플레이 되고 있는 노래 정보 구하기"
    
    current_song = jukebox.current_song()
    ret = { 'code': 0, 'msg': 'ok' }
    if current_song:
        ret['song'] = current_song.to_dict()

    # 최종 정보는
    # - code
    # - msg
    # - songs
    return jsonify(**ret)
    
@app.route('/jukebox/songs', methods=['POST'])
def add_song():
    """노래 추가.

    youtube link를 주면 곡 정보를 DB에 추가한다.
    가능한 링크
      - youtube 노래 link
      - youtube playlist link
    """

    # web browser에서 요청한 데이터를 받는다. body 영역 데이터
    data = request.get_json(silent=True)

    # 그중에 url, list_url, add_playlist 정보를 가져온다.
    # url는 노래 link
    # list_url는 플레이 리스트 link
    # add_playlist는 현재 연주되고 있는 플레이 리스트에 바로 추가할지 결정
    url = data.get("url", None)
    list_url = data.get("list_url", None)
    add_playlist = data.get('add_playlist', False)

    # 노래 link 라면
    if url:

        # 노래 정보를 구해서
        info = youtube.get_video_info(url)
        # song 객체로 만들어
        song = Song()
        song.url = info["url"]
        song.uid = info["uid"]
        song.title = info["title"]
        song.img_url = info["image_url"]
        song.duration = info['duration']

        if song.title and song.duration:
            # 데이터가 valid 할 때만 추가
        
            # DB에 추가한다.
            jukebox.append_song_to_db(song)

            # 플레이 리스트에 추가해야 하면 그렇게 한다.
            if add_playlist:
                jukebox.append_song_playlist(song)

    elif list_url:
        # 노래 목록이면
        # 별도의 처리 쓰레드를 통해서 처리한다.
        thread = AddYoutubeListThread(jukebox, list_url, add_playlist)
        thread.start()

    # 잘 처리되었다고 반환
    ret = { 'code': 0, 'msg': 'ok' }        
    return jsonify(**ret)


@app.route('/jukebox/playlist', methods=['POST'])
def add_playlist():
    """플레이 리스트에 노래 추가

    여기에 추가된 노래의 dbid를 파라미터로 받는다
    """

    # dbid 정보를 가져온다.
    data = request.get_json(silent=True)
    dbid = data['dbid']
    
    if dbid:
        # dbid에 해당하는 노래를 찾아서 추가한다.
        jukebox.append_playlist_song_by_dbid(dbid)

    # 결과 반환
    ret = { 'code': 0, 'msg': 'ok' }        
    return jsonify(**ret)
        
    

@app.route('/jukebox/control/<cmd>', methods=['POST'])
def command(cmd):
    """Jukebox 명령 처리
    
    명령:
      - play    다시 플레이
      - stop    현재곡 중지
      - next    다음곡
    """
    ret = { 'code': 0, 'msg': 'ok' }

    if cmd == 'play':
        jukebox.play()
    elif cmd == 'stop':
        jukebox.stop()
    elif cmd == 'next':
        jukebox.forward()
    else:
        ret = { 'code': 100, 'msg': 'not supported command ' + cmd }        
    
    return jsonify(**ret)
    

#--------------------
# 템플릿에서 사용할 필터
#--------------------

@app.template_filter('duration_time')
def _jinja2_filter_datetime(seconds, fmt=None):
    """duration 시간 표시

    200 => 3:20
    """
    seconds = int(seconds)
    ret = []
    while seconds:
        if seconds < 60:
            ret.insert(0,'%02d' % seconds)
            break

        ret.append('%02d' % (seconds % 60))
        seconds = seconds // 60
        
    return ':'.join(map(str,ret))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
