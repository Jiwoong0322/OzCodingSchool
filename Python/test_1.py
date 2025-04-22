# requests는 서버에 요청을 보낸다.
import requests

keyword = input("검색할 키워드를 입력해주세요")

url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="

html = requests.get(url+keyword) #get 요청이란 주소를 입력하면 사이트에 접속이 가능하도록 화면을 구성할 수 있는 html, css js코드를 가져와라.
print(html.text)