import pandas as pd
import numpy as np
df = pd.DataFrame({'가입월' : [1,1,1,2,2,3], '탈퇴월' : [1,2,3,2,3,3], '탈퇴회원수' : [101,52,30,120,60,130]})

# 피벗 테이블
pivot = pd.pivot_table(df, values= '탈퇴회원수',index=['가입월'], columns= ['탈퇴월'])
# print(pivot)
pivot = pd.pivot_table(df, values= '탈퇴회원수',index=['가입월'], columns= ['탈퇴월'], fill_value=0)
print(pivot)

# Quiz 각 상품 항목 별 크기 별로 판매 개수와 판매 금액의 합을 구하시오
import random

a = []
b = []

for i in range(100):
    a.append(random.randint(1,3)) # 1,2,3 중 무작위
    b.append(random.randint(1,3))

df = pd.DataFrame({'품목' : a, '크기' : b})
df['금액'] = df['품목'] * df['크기' * 500]
df['수수료'] = df['금액'] * 0.1

name = {1:'토마토', 2:'바나나', 3:'사과'}
size = {1:'소', 2:'중', 3:'대'}
df['품목'] = df['품목'].map(name)
df['크기'] = df['크기'].map(size)

pd.pivot_table(df, values= '금액', index=['품목'], columns= ['크기'], aggfunc=('count', 'sum'))

# Quiz 각 상품 항목 별 크기 별로 판매 개수와 판매 금액/수수료의 합을 구하시오
pd.pivot_table(df, index=['품목'], columns= ['크기'], aggfunc={'금액' : ['count', 'sum'], '수수료' : 'sum'})