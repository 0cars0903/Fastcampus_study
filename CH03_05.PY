import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1,11)], 'b' : [i for i in range(11,21)], 'c' : [i for i in range(21,31)]})
# print(df)

# 두 개 이상의 columus 추출
b = df[['a','b']]
# print(b)

# 첫번째 행 데이터 추출
c = df.loc[0]
# print(c)

# 슬라이스
d = df.loc[2:4] # index 값 포함
# print(d)

# index가 문자로 이루어진 데이터 프레임 생성
index = ['a','b','c','d','e','f','g','g','h','i']
df = pd.DataFrame({'a' : [i for i in range(1,11)], 'b' : [i for i in range(11,21)], 'c' : [i for i in range(21,31)]}, index=index)
# print(df)
e = df.loc['g']
print(e)
df.loc['C':] # data가 쌓여진 순서대로 출력된다. (알파벳 순서가 아님!)

# 열과 인덱스를 찾기
df.loc[['g','i'],['a','c']]

# iloc
# 처음부터 5열까지 , 0번째, 2번재의 데이터
df.iloc[:5, [0,2]]