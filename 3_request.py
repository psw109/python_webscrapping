# %%
import requests

res = requests.get("http://naver.com")
print(f'응답코드 : {res}') #200이면 정상 출력

# %%
res1 = requests.get("http://naru.com")
print(f'응답코드 : {res1}') #404 비정상 출력

# %%
if res.status_code == requests.codes.ok:
    print("normal")
else:
    print(f"error code : {res.status_code}")
    
# %%
try :
    res1.raise_for_status() #위 if문을 한번에 확인할수 있음 
except:
    print('error')

# %%
print(len(res.text))

# %%
res3 = requests.get('http://goolge.com')
print(len(res.text))

# %%
with open("mygoogle.html", "w", encoding='utf-8') as f:
    f.write(res3.text)
