import mechanicalsoup

browser = mechanicalsoup.Browser()                  #<---- 1

# 여기에 자신의 ID/PW를 입력한다.
user_id = '<ID 입력>'                               #<---- 2
user_pw = '<암호 입력>'                             #<---- 3

# 로그인 페이지
login_page = browser.get("https://github.com/login")   #<---- 4

# login_page.soup 는 BeautifulSoup이 적용된 객체
# BeautifulSoup의 select()를 이용해서 
# 로그인 폼을 찾는다.
login_form = login_page.soup.select("#login")[0].select("form")[0]    #<---- 5

# ID / PW 입력
login_form.select("#login_field")[0]['value'] = user_id               #<---- 6
login_form.select("#password")[0]['value'] = user_pw                  #<---- 7

# 데이터를 전송하고 로그인 결과를 받는다.
page2 = browser.submit(login_form, login_page.url)                    #<---- 8

# 로그인 되었는지 확인한다.
messages = page2.soup.select('div.dropdown-header.header-nav-current-user.css-truncate')[0]  #<---- 9
if messages:
    print(messages.text)                                              #<---- 10
