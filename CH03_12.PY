import pandas as pd
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'c' : [21,22,23]})
df2 = pd.DataFrame({'A' : [4,5,6], 'B' : [14,15,16], 'c' : [24,25,26]})

# 상하 결합
pd.concat([df1,df2],ignore_index = True) # ignore_index = True

# 필드 순서가 섞인 경우 : 정렬되어 결합된다.
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'c' : [21,22,23]})
df2 = pd.DataFrame({'B' : [4,5,6], 'A' : [14,15,16], 'c' : [24,25,26]})
pd.concat([df1,df2],ignore_index = True)

# 서로 다른 필드로 구성되어 있는 데이터 프레임 결합
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23], 'D' : [31,32,33]})
df2 = pd.DataFrame({'B' : [4,5,6], 'A' : [14,15,16], 'C' : [24,25,26], 'E' : [41,42,43]})
pd.concat([df1,df2])
pd.concat([df1,df2], join='outer') # 서로 다른 필드 포함
pd.concat([df1,df2], join='inner') # 서로 다른 필드는 제거