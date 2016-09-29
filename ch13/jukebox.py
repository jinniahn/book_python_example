import sys

import youtube
import threading
import queue
from player import MusicPlayer
from song import Song
from store import Store
import time

# 음악 플레이 리스트
playlist_lock = threading.Lock()
playlist = []

# 명령 큐
command_list = queue.Queue()

class AsyncMusicPlayer(threading.Thread):
    '''Music Player.
    
    MusicPlayer가 동기적이기 때문에 이것을 비동기적으로 명령을 처리
    하기 위해서 Thread로 만듬

    외부와의 데이터 교환:
    - playlist        : 플레이 리스트
    - command_list    : 명령 수행
    '''

    def __init__(self):
        threading.Thread.__init__(self)

        # 현재 플레이 중인 Url
        self.url = ''
        # 현재 플레이 되고 있는 노래
        self.current_song = None

        # webbrowser player 인스턴스
        self.player = MusicPlayer()

        # DB
        self.store = Store()

    def run(self):
        '이 쓰레드에서 수행할 로직'

        while True:
            try:
                # 0.5초를 주기로 명령 수행
                time.sleep(0.5)

                # 광고가 나오는지 확인해서 넘긴다.
                # 보통 youtube 광고는 5초다.
                # TODO: 광고가 나오면 volume을 줄이도록 한다.
                self.player.skip_if_exists_ad()

                if self.url == '':
                    self.play_next_song()
                
                # URL이 변경되었으면 표시한다.
                url = self.player.current_url()
                if( self.url != url ):
                    self.url = url
                    # TODO:
                    #   - 여기에서 곡을 추가하는 로직을 넣으면
                    #   - 내가 듣는 링크를 플레이 리스트로 만들 수 있다.
                    print(self.url)
                    
                # 노래가 중지되면 다음 노래
                if self.player.is_finished() :

                    # played_count 수를 하나 증가 시킨다.
                    if self.current_song:
                        self.current_song.played_count += 1
                        self.store.update(self.current_song)

                    self.play_next_song()
                elif self.player.is_unplable():
                    self.play_next_song()
                    
                self.handle_cmd();
            except queue.Empty:
                pass
            except Exception as e:
                # 에러가 발생하면 에러의 종료를 출력
                print(type(e))
                print(e)

    def play_next_song(self):
        " 다음 곡 "

        # 플레이 리스트에서 하나 꺼낸다.
        playlist_lock.acquire()
        try:
            song = playlist.pop(0)
            url = song.url
        except:
            url = None
        playlist_lock.release()

        # url이 있으면 다음곡 플레이
        if url:
            self.current_song = song
            self.player.play_url(song.url)

    def stop(self):
        " 일시 정지 "
        self.player.stop()

    def play(self):
        " 다시 플레이"
        self.player.play()

    def handle_cmd(self):
        "명령 처리"
        data = command_list.get(block=False)
        if data:
            cmd, param = data
            if cmd == 'forward':
                self.play_next_song()
            elif cmd == 'stop':
                self.stop()
            elif cmd == 'play':
                self.play()

class JukeBox(object):
    ''' 쥬크박스.

    기능:
     - 음악리스트를 관리한다.
     - 랜덤플레이를 지원한다.
     - 자동플레이를 지원한다.
     - 현재 실행 중인 곡을 알 수 있다.

    '''

    
    music_player = None

    def __init__(self):
        if JukeBox.music_player == None:
            JukeBox.music_player = AsyncMusicPlayer()
            JukeBox.music_player.start()
        self.store = Store()
        
        songs = self.store.get_songs()
        self.append_song_list(songs)

    def append_song_to_db(self, song):
        self.store.update_or_new(song)        

    def append_song_list(self, songs):
        for song in songs:
            self.append_song_playlist(song)

    def append_song_playlist(self, song):
        playlist_lock.acquire()
        playlist.append(song)
        playlist_lock.release()

    def append_playlist_song_by_dbid(self, dbid):
        song = self.store.find_by_id(dbid)
        playlist_lock.acquire()
        playlist.append(song)
        playlist_lock.release()

    def play_right_next(self, song):
        playlist_lock.acquire()
        playlist.insert(0, song)        
        playlist.append(song)

    def current_song(self):
        return self.music_player.current_song

    def current_playlist(self):
        playlist_lock.acquire()
        songs = playlist[:]
        playlist_lock.release()
        
        return songs

    def get_db_songs(self):
        return self.store.get_songs()

    def stop(self):
        print("stop in juke box")
        cmd = ('stop',None)
        command_list.put(cmd)

    def play(self):
        cmd = ('play',None)
        command_list.put(cmd)

    def forward(self):
        cmd = ('forward',None)
        command_list.put(cmd)

    def rewind(self):
        pass

    def clear(self):
        playlist_lock.acquire()
        playlist.clear()
        playlist.append(song)

        self.store.remove_all()

class AddYoutubeListThread(threading.Thread):
    def __init__(self, jukebox, list_url, add_playlist):
        threading.Thread.__init__(self)
        self.jukebox = jukebox
        self.list_url = list_url
        self.add_playlist = add_playlist
        self.store = Store()

    def run(self):
        infos = youtube.get_video_infos_from_list(self.list_url)
        for info in infos:
            print(info)
            try:
                song = Song()
                song.url = info["url"]
                song.uid = info["uid"]
                song.title = info["title"]
                song.img_url = info["image_url"]
                song.duration = info['duration']

                if song.title and song.duration:
                    # 데이터가 valid 할 때만 추가
                    
                    self.store.update_or_new(song)

                    if self.add_playlist:
                        self.jukebox.append_song_playlist(song)
                
            except Exception as e:
                print(e)

def test():
    player = JukeBox()

    # player.clear()

    # song = Song()
    # song.title = 'Justin Bieber - Sorry (PURPOSE : The Movement)'
    # song.url = 'https://www.youtube.com/watch?v=fRh_vgS2dFE'
    # song.uid = 'fRh_vgS2dFE'
    # player.append_song_list(song)

    # song = Song()
    # song.title = 'Rihanna - Work (Explicit) ft. Drake'
    # song.url = 'https://www.youtube.com/watch?v=HL1UzIK-flA'
    # song.uid = 'HL1UzIK-flA'

    # player.append_song_list(song)

    while True:
        time.sleep(1)
    

if __name__ == '__main__':
    test()
    
