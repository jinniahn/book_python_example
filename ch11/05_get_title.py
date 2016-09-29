import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.naver.com')
soup = BeautifulSoup(res.text)
tags = soup.select('title')
if tags:
    print(tags[0].text)
