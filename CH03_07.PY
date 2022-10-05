import pandas as pd
df = pd.DataFrame({'a' : [2,3,2,7,4], 'b' : [2,1,3,5,3], 'c' : [1,1,2,3,5]})
# print(df)

# index 기준 정렬
df.sort_index()
# print(df.sort_index())

# 내림차순
df.sort_index(ascending=False) # inplace = Ture
# print(df.sort_index(ascending=False))

# index 초기화
df.reset_index() # 기존의 index도 같이 출력
df.reset_index(drop=True) # 기존 index 제거
df.reset_index(drop=True, inplace=True)

# Value 기준 정렬
df = pd.DataFrame({'a' : [2,3,2,7,4], 'b' : [2,1,3,5,3], 'c' : [1,1,2,3,5]})
# print(df)
df.sort_values(by='a') # a열 기준으로 오름차순 정렬, inplace=True

# 내림차순
df.sort_values(by='a', ascending=False) # inplace=True

# 2개의 기준
df.sort_values(by=['a','b'])

# a는 오름차순, b는 내림차순
df.sort_values(by=['a','b'], ascending=[True, False], inplace=True)
df.reset_index(drop=True, inplace=True)
