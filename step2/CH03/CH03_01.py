import pandas as pd
import numpy as np
# data frame method
# method 1
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})

# method 2
dummy = {'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]}
df2 = pd.DataFrame(dummy)

# method 3
a = [[1,2,3],[4,5,6],[7,8,9]]
df3 = pd.DataFrame(a)

df3.columns = ['a','b','c']

b= {'company' : ['abc', '회사', '123'],'직원수' : ['400','10','6']}
df4 = pd.DataFrame(b)

c = {'company' : ['abc', '회사', '123'],'직원수' : ['400','10','6'], '위치' : ['서울', np.NaN, '부산']}
df5 = pd.DataFrame(c)
print(df5)
