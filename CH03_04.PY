import pandas as pd
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})

# a 열의 추출
df['a']

# 시리즈 생성방법
a = pd.Series([1,2,3,1,2,3])
# 시리즈는 한 열씩만 생성 가능하다.

# index 변경
a = pd.Series([1,2,3,1,2,3], index= ['a','b','c','d','e','f'])
# index 길이는 맞춰주어야 한다.
a['e'] # 2

# 유일한 값 찾기
df = pd.DataFrame({'a' : [1,2,3,1,2,3], 'b' : [4,5,6,6,7,8], 'c' : [7,8,9,10,11,12]})
a = df['a']
a.unique() # 유일한 값 찾기
a.unique()[2]