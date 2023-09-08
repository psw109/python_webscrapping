# %% 현재 실습 불가능
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index" # 네이버 웹툰
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") #html 문서를 lxml parser을 통해 soup객체를 만든다
print(soup.title)
print(soup.title.get_text())
print(soup.body) # naver html구조가 바껴서 body구조를 볼 수 없음 다른 페이지로 실습해야함

# %% 네이버 웹툰대신 네이버 증권 홈페이지로 실습

url = "https://finance.naver.com" # 네이버 증권

res = requests.get(url)
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml")
print(soup.title)
print(soup.title.get_text())
print(soup.a) # soup 객체에서 처음 발견되는 a element를 반환
print(soup.a.attrs)
print(soup.a["href"]) # a element의 속성 정보를 출력 

# %%

print(soup.find("span", attrs = {"class" : "tx"})) #span element중 class 속성이 tx인 값들 중 첫번째를 찾는다
print(soup.find(attrs = {"class" : "tx"})) # class : tx테그가 붙은 element는 span만 있을것으로 추측