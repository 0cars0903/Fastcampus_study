import pandas as pd
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})

# 칼럼명 얻기
df.columns

# index
df.columns(1)

# 치환
df.columns = ['d','e','f']

# rename
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})
df.rename(columns={'d' : '디'}, inplace=True) # inplace=True 해주어야 저장된다. 