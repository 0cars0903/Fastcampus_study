import pandas as pd
import numpy as np
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,np.nan,3,4], 'c' : [3,4,7,6,4]})
# print(df)

# 결측 유무 확인
df.isnull()
# print(df.isnull())

# 결측값 개수 확인
df.isnull().sum()
# print(df.isnull().sum())
# print(df.isnull().count()) 

# 결측값 포함된 행 제거
df.dropna(inplace=True)
df.dropna(axis=1, inplace=True)

# 결측값을 대체하기
df = pd.DataFrame({'a' : [1,1,3,4,5], 'b' : [2,3,np.nan,3,4], 'c' : [3,4,7,6,4]})
df.fillna(0,inplace=True)

# 앞이나 뒤의 숫자로 교체
df = pd.DataFrame({'a' : [1,1,3,4,np.nan], 'b' : [2,3,np.nan,np.nan,4], 'c' : [np.nan,4,1,1,4]})

# 뒤의 값으로 채우기
df.fillna(method='bfill') # inplace=True

# 앞의 값으로 채우기
df.fillna(method='ffill') # inplace=True

# limit 설정
df.fillna(method='ffill', limit=1)

# 평균으로 대체
df = pd.DataFrame({'a' : [1,1,3,4,np.nan], 'b' : [2,3,np.nan,np.nan,4], 'c' : [np.nan,4,1,1,4]})
df.mean()['a'] # 평균계산
df.fillna(df.mean()['a'])
df.mean()
df.fillna(df.mean()) # 각 열의 평균값을 결측값에 대입