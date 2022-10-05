import pandas as pd
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})
# print(df)

# 칼럼 추가
df['d'] = [1,3,6,4,8] # 칼럼 추가
df['e'] = 1 # 중복값 입력 시
df['f'] = df['a'] + df['b'] - df['c'] # 칼럼 간의 연산
# print(df)

# 칼럼 삭제
df.drop(['d', 'e', 'f'], axis=1, inplace=True)
# print(df)

# 레코드 추가
df.append({'a' : 6, 'b' : 7, 'c' : 8}, ignore_index=True) # inplace 사용 X
# print(df)
df.loc[6] = [7,8,9]
# print(df)

# 레코드 삭제
# df.drop(0)
# df.drop(0,1)

df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})
df.drop(i for i in range(4))
df.drop(df.index[:4]) # 좀 더 정확한 방법

# a가 4미만인 레코드 삭제
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})
df[df['a'] < 4].index
df = df.drop(df[df['a'] < 4].index)
# print(df)

# a가 3미만, c가 4인 레코드 삭제
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,2,3,4], 'c' : [3,4,7,6,4]})
df[(df['a']<3) & (df['c']==4)].index
df = df.drop(df[(df['a']<3) & (df['c']==4)].index)
print(df)