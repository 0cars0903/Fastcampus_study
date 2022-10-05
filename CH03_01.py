from multiprocessing import dummy
import pandas as pd
df = pd.DataFrame({'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]})
print(type(df))
print(df)
dummy = {'a' : [1,2,3], 'b' : [4,5,6], 'c' : [7,8,9]}
df2 = pd.DataFrame(dummy)
print(df2)