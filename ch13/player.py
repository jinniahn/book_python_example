'''
TODO:

 - handle : NoSuchWindowException
'''

import time
import sys
import os.path
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# 현재 모듈 위치
curdir = os.path.join(os.path.dirname(__file__))

# 음악 플레이어
class MusicPlayer(object):
    def __init__(self):
        self.driver = self._create_webdriver()

    def _create_webdriver(self):
        if sys.platform == 'darwin':
            driver = webdriver.Chrome(os.path.join(curdir, 'webdriver', 'mac', "chromedriver"))
        elif sys.platform.startswith('linux'):
            driver = webdriver.Chrome(os.path.join(curdir, 'webdriver', 'linux32', "chromedriver"))
        elif sys.platform.startswith('win'):
            driver = webdriver.Chrome(os.path.join(curdir, 'webdriver', 'win', "chromedriver.exe"))
        else:
            raise Exception('not support platform ' + sys.platform)
        return driver

    def _injectJquery(self):
        is_existed_jquery = self._exec_js('return !!window.jQuery')
        if not is_existed_jquery:
            #print('inject jquery')
            with open(os.path.join(curdir, 'jquery', 'jquery-3.3.1.js')) as f:
                try:
                    self._exec_js(f.read())
                except Exception as f:
                    print(f)

    def current_url(self):
        return self._exec_js('return location.toString()')

    def skip_if_exists_ad(self):
        try:

            self._exec_js('jQuery(".adDisplay").hide()')
            element = self.driver.find_element_by_css_selector(".videoAdUiSkipButton.videoAdUiAction")
            if element:
                #print("click")
                element.click()
                
        except Exception as e:
            pass
            #print(e)

    def is_loaded(self):
        ret = self._exec_js('''
        return (function(){
        try{
        var v = jQuery(".video-stream.html5-main-video")[0];
        return !!v;
        }catch(e){
        return false;
        }
        })();
        ''')
        return ret

    def is_unplable(self):
        '''어떤 이유로건 플레이 하지 못하는지 확인한다.'''
        
        ret = self._exec_js('''
        return (function(){
        try{
        var v = jQuery("#unavailable-submessage").text().trim();
        return v != '';
        }catch(e){
        return false;
        }
        })();
        ''')

        return ret
        

    def is_finished(self):
        ret = self._exec_js('''
        return (function(){
        try{
        var v = jQuery(".video-stream.html5-main-video")[0];
        return v.duration > 0 && v.currentTime == v.duration;
        }catch(e){
        return false;
        }
        })();
        ''')

        return ret

    def play_url(self, url):
        self.driver.get(url)
        #time.sleep(1)
        for _ in range(10):
            time.sleep(0.5)
            if self.is_loaded():
                print('loaded')
                break

    def _exec_js(self, js):
        try:
            ret = self.driver.execute_script(js)
            return ret
        except Exception as e:
            if 'jQuery' in e.msg:
                self._injectJquery()
                return self._exec_js(js)
            print(type(e))
            print(e)
            

    def play(self):
        self._exec_js('jQuery(".video-stream.html5-main-video")[0].play()')

    def stop(self):
        print('stop in player');
        print(self._exec_js('return jQuery(".video-stream.html5-main-video")[0].pause();'))


def play_starbuck_songs():
    """test music player.

    play starbuck songs to test musicplayer.
    """

    import time
    
    url = 'https://www.youtube.com/watch?v=z-sWrPBgiF0'

    player = MusicPlayer()
    player.play_url(url)

    cur_url = None

    count = 0
    while True:
        try:
            #count += 1
            if( count < 10 ) :
                player.skip_if_exists_ad()
                url = player.current_url()
                if( cur_url != url ):
                    cur_url = url
                    print(cur_url)

            #if( count == 20 ):
                #player.stop()

            #if( count == 30 ):
                #player.play()
                
            time.sleep(1)

            if player.is_unplable():
                print('unplable')
        except:
            break

        
if __name__ == '__main__':
    play_starbuck_songs()
    

    
    
