import pandas as pd
df = pd.DataFrame({'a' : [i for i in range(1,11)], 'b' : [i for i in range(11,21)], 'c' : [i for i in range(21,31)]})
# print(df)

# 조건에 맞는 데이터 추출
# a가 3이상인 데이터 추출
a = df[df['a']>=3]
# print(a)

# a가 3이상인 데이터에서 a, c 열만 출력
a = df[df['a']>=3][['a','c']]
# print(a)

# a 3이상, b는 16미만
a = df[(df['a']>=3) & (df['b']<16)] 
# print(a)

# a = (df['a']>=3) & (df['b']<16)
# print(a)

# 3 이하 이거나 7 이상
df = pd.DataFrame({'a' : [i for i in range(1,11)], 'b' : [i for i in range(11,21)], 'c' : [i for i in range(21,31)]})
a = df[(df['a']<=3) | (df['a']>=7)]
# print(a)

# a 3이상이고 b가 16미만 이거나 c가 30인 데이터를 출력
df = pd.DataFrame({'a' : [i for i in range(1,11)], 'b' : [i for i in range(11,21)], 'c' : [i for i in range(21,31)]})
a = df[(df['a']>=3) & (df['b']<16) | (df['c'] == 30)]
print(a)