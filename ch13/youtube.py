'''
Youtube 정보 조회
=================

- youtube URL를 통해서 youtube 정보를 조회한다.
  - title
  - duration
  - description
  - img_url
- youtube playlist 목록에서 각 항목의 정보를 조회한다.
- youtube url을 분석해서 uid를 얻는다.
- uid를 통해서 youtube url을 생성한다.
'''

from urllib.parse import *
import requests                     # HTML 다운로드
from pyquery import PyQuery as pq   # HTML 분석용.
from pprint import pprint

def get_uid_from_url(url):
    '''url에서 uid 추출.
    
    - 일반 노래인 경우
       - ex: https://www.youtube.com/watch?v=HHP5MKgK0o8'
       - return: {'uid': 'HHP5MKgK0o8'}
    - 리스트인 경우
       - ex: https://www.youtube.com/watch?v=fRh_vgS2dFE&list=PLDcnymzs18LVXfO_x0Ei0R24qDbVtyy66
       - return: {'list': 'PLDcnymzs18LVXfO_x0Ei0R24qDbVtyy66', 'uid': 'fRh_vgS2dFE'}
    '''
    ret = {}
    u = urlparse(url)
    if u.netloc == 'www.youtube.com':
        qs = parse_qs(u.query)
        if 'v' in qs:
            ret['uid'] = qs['v'][0]
        if 'list' in qs:
            ret['list'] = qs['list'][0]
    elif u.netloc == 'youtu.be':
        if u.path:
            ret['uid'] = u.path[1:]
    return ret
            
def get_url_with(uid):
    'uid를 주면 해당 동영상을 볼 수 있는 url 생성'
    return 'https://www.youtube.com/watch?v={}'.format(uid)


def get_video_info(url):
    ''' 정보 추출
    
    - title
    - description
    - image_url
    '''

    uid = get_uid_from_url(url)
    # youtube URL이 아니면 그냥 리턴
    if not uid: return {}

    # youtube URL이 맞으면 url을 새로 만든다.
    # list정보가 들어 있으면 여기서 제거된다.
    url = get_url_with(uid['uid'])

    # 데이터 가져오고
    resp = requests.get(url)
    h = pq(resp.text)

    # 정보 추출
    n = h('meta[property="og:title"]')
    title = n and n[0].attrib['content'] or ''
    n = h('meta[property="og:description"]')
    content = n and n[0].attrib['content'] or ''
    n = h('meta[property="og:image"]')
    img_url = n and n[0].attrib['content'] or ''
    n = h('span.video-time')
    duration = n and n[0].text or 0
    if duration:
        duration = list( map(str.strip,duration.split(':')) )
        t = 0
        for d in duration[:]:
            t = t * 60 + int(d)
        duration = t


    # 반환할 데이터 준비
    ret = {}
    ret["url"] = url
    ret["uid"] = uid["uid"]
    ret["title"] = title
    ret["description"] = content
    ret["image_url"] = img_url
    ret['duration'] = duration

    return ret

def get_video_infos_from_list(url):
    """youtube의 playlist 정보를 조회.

    youtube의 playlist가 포함된 URL에서 등록된 url에서 정보를 조회한다.
    """
    # url이 플레이 리스트인지 확인한다.
    id_info = get_uid_from_url(url)
    if 'list' not in id_info:
        # 리스트가 아니면 하나의 정보만 반환
        return [get_video_info(url)]

    print(url)

    resp = requests.get(url)
    h = pq(resp.text)

    items = h('#playlist-autoscroll-list li')
    for item in items:
        vid = item.attrib['data-video-id']
        url = get_url_with(vid)
        try:
            yield get_video_info(url)
        except Exception as e:
            print('cannot get info from ' + url)
            print(e)


def test_get_infos_from_list():
    url = 'https://www.youtube.com/watch?v=bZqnqH9s1jk&index=8&list=PLqrCGHzWbat_ggH1lOdm0lADN4Q91kgt7'
    infos = get_video_infos_from_list(url)
    for info in infos:
        print(info)
        
def test_get_video_info():
    u1 = 'https://www.youtube.com/watch?v=HHP5MKgK0o8'    
    info = get_video_info(u1)
    print(info)

def test_get_uid_from_url():
    u1 = 'https://www.youtube.com/watch?v=HHP5MKgK0o8'
    u2 = 'https://youtu.be/fRh_vgS2dFE'
    u3 = 'https://www.youtube.com/watch?v=fRh_vgS2dFE&list=PLDcnymzs18LVXfO_x0Ei0R24qDbVtyy66'

    print(get_uid_from_url(u1))
    print(get_uid_from_url(u2))
    print(get_uid_from_url(u3))

def test_err_url():
    url = 'https://www.youtube.com/watch?v=UBWCJ4-evrg&list=RDUBWCJ4-evrg' ##t=2899'
    info = get_video_info(url)
    print(info)
    
if __name__ == '__main__':
    test_get_infos_from_list()
