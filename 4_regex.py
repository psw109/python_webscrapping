# %% 

import re

p1 = re.compile('ca.e') # . : one string
p2 = re.compile('^de') # ^ : string start 'de' => desk / destiny
p3 = re.compile("se$") # $ : string end 'se' => case / base

m1_1 = p1.match("careless")
m1_2 = p1.match("caffe")
m2 = p2.match('desk')
m3 = p3.match("abdse")

print(m1_1)
print(m1_2)
print(m2)
print(m3) #match는 문자열 처음부터 찾는 메소드 이기때문에 / search는 가능
# %%
print(m1_1.group())
if m1_2:
    print(m1_2.group())
else:
    print('no match')
# %% 함수화

def print_match(m):
    if m:
        print(f'm.group() : {m.group()}') # 일치하는 문자열 반환
        print(f'm.string : {m.string}') # 입력받은 문자열
        print(f"m.start() : {m.start()}") # 일치하는 문자열 시작 index
        print(f"m.end() : {m.end()}") # 일치하는 문자열 끝 index
        print(f"m.span() : {m.span()}") # 일치하는 문자열 시작, 끝 index
    else:
        print('no match')   
# %%

m2 = p2.match('desk')
print_match(m2)

# %%

m1_3 = p1.search("good care") 
print_match(m1_3) # 주어진 문자열의 일부만 맞아도 잘 출력됨

m1_4 = p1.match('good care')
print_match(m1_4) # match는 주어진 문자열이 처음부터 매치해야함

# %%

m_list = p1.findall('careless') #일치하는 모든 것을 리스트로 반환
print(m_list)

m_list2 = p1.findall('good care cafe cafecafe')
print(m_list2)

# %% 정규식 사용법

# 1. p = re.compile('regexpress')
# 2. m = p.match('compare string')
# 3. m = p.search('compare string')
# 4. m_list = p.findall('compare string')