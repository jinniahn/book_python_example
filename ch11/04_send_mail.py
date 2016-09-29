#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import requests
r = requests.get('https://en.wikipedia.org/wiki/Main_Page')
html_doc = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')

css_path = '#mp-otd > ul > li > a'
tags = soup.select(css_path)

ret = []
for tag in tags:
    year = tag["title"]
    desc = tag.parent.get_text().split('–',1)[1]
    ret.append("{}: {}".format(year, desc))

# Mail로 내용을 전달한다
mail_url = "<url>"
mail_key = "<api_key>"
from_user = '<user>'

requests.post(
    mail_url,
    auth=("api", mail_key),
    data={"from": from_user,
          "to": ["jinniahn@gmail.com"],
          "subject": "과거의 오늘에는 어떤 일들이 있을까?",
          "text": "\n".join(ret)})
