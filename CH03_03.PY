import pandas as pd
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})

# 복제
df2 = df
# df를 변경하면 df2도 변경된다.

import copy
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})
df2 = copy.deepcopy(df)
