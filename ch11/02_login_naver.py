#!/usr/bin/env python3

import re
import requests
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def naver_login(nid, npw):
    naver_url = 'https://nid.naver.com/nidlogin.login'
    
    driver = webdriver.PhantomJS()
    #driver = webdriver.Firefox();
    
    driver.get(naver_url)
    driver.set_window_size(1024,768)

    # selenimum manual
    # 주로 CSS selection을 사용
    # http://selenium-python.readthedocs.io/navigating.html
    text_id = driver.find_element_by_css_selector('#id.int')
    text_id.send_keys(nid)
    
    text_pw = driver.find_element_by_css_selector("#pw.int")
    text_pw.send_keys(npw)
    
    bt_login = driver.find_element_by_css_selector('#frmNIDLogin input.int_jogin')
    bt_login.click()


    # 네이버 본 화면으로 넘어갈 때까지 기다린다.
    # time.sleep(2)로 얼마간 기다려도 된다.
    # http://selenium-python.readthedocs.io/waits.html
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.title_is('NAVER'))

    # 쿠키를 dict 타입으로 간략화 한다.
    cookies = {}
    for c in driver.get_cookies():
        cookies[c['name']] = c['value']
        
    driver.close()
    return cookies

user_id = '아이디'
user_pw = '암호'

try:
    # login 후 쿠키값을 가져온다.
    cookies = naver_login(user_id, user_pw)
    # 쿠키각을 노트 정보가 가져올 때 포함시킨다.
    resp = requests.get('http://note.naver.com/', cookies = cookies)
    body = resp.text

    # HTML에서 노트 갯수가 들어 있는 문자열을 찾는다.
    m = re.search(r'"inboxTotalCount":(\d*),', body)
    if m:
        print(m.group(1))
except:
    print('cannot login')
