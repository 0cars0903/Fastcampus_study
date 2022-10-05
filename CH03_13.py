import pandas as pd
df1 = pd.DataFrame({'A' : [1,2,3], 'B' : [11,12,13], 'C' : [21,22,23], 'D' : [31,32,33]})
df2 = pd.DataFrame({'E' : [4,5,6], 'F' : [14,15,16], 'G' : [24,25,26], 'H' : [41,42,43]})

# 좌우결합
pd.concat([df1, df2], axis=1)

df1 = pd.DataFrame({'ID' : [1,2,3], '성별' : ['F','M','F'], '나이' : [20,30,40]})
df2 = pd.DataFrame({'ID' : [1,2,3], '키' : [160.5,170.3,181.1], '몸무게' : [45.1,50.3,72.1]})
df = pd.concat([df1, df2], axis=1)

df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '성별' : ['F','M','F','M','F'], '나이' : [20,30,40,25,42]})
df2 = pd.DataFrame({'ID' : [3,4,5,6,7], '키' : [160.5,170.3,181.1,142.5,153.7], '몸무게' : [45.1,50.3,72.1,38,42]})
pd.concat([df1, df2], axis=1) # 1대 1 매칭이 되지 않음

# 성별과 나이가 확인된 유저들 대상
df = pd.merge(df1, df2, how = 'left', on = 'ID')

# 키와 몸무게가 확인된 유저들 대상
df = pd.merge(df2, df1, how = 'left', on = 'ID')
pd.merge(df1, df2, how = 'right', on = 'ID')

# 성별, 나이, 키, 몸무게 모두 확인된 유저들 대상
df = pd.merge(df1, df2, how = 'inner', on = 'ID')

# 모든 유저 정보 출력
df = pd.merge(df1, df2, how = 'outer', on = 'ID')

df1 = pd.DataFrame({'USER_ID' : [1,2,3,4,5], '성별' : ['F','M','F','M','F'], '나이' : [20,30,40,25,42]})
df2 = pd.DataFrame({'ID' : [3,4,5,6,7], '키' : [160.5,170.3,181.1,142.5,153.7], '몸무게' : [45.1,50.3,72.1,38,42]})
df = pd.merge(df1, df2, how = 'outer', left_on = 'USER_ID', right_on= 'ID')

# Quiz 
df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '가입일' : ['2021-01-02','2021-01-04','2021-01-10','2021-02-10','2021-02-24'],
                    '성별' : ['F','M','F','F','M']})
df2 = pd.DataFrame({'구매순서' : [1,2,3,4,5], 'ID' : [1,1,2,2,3], '금액' : [1000,1500,2000,3000,4000]})
pd.merge(df1, df2, how = 'left', on = 'ID')