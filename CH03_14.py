import pandas as pd
df1 = pd.DataFrame({'ID' : [1,2,3,4,5], '가입일' : ['2021-01-02','2021-01-04','2021-01-10','2021-02-10','2021-02-24'],
                    '성별' : ['F','M','F','F','M']})
df2 = pd.DataFrame({'구매순서' : [1,2,3,4,5], 'ID' : [1,1,2,4,1], '구매월' : [1,1,2,2,3], 
                    '금액' : [1000,1500,2000,3000,4000]})
df = pd.merge(df1, df2, how = 'left', on = 'ID')
# print(df)

# 회원 별 누적 금액 계산
df_sum = df2.groupby(by = ['ID'])['금액'].sum()
# print(df_sum)
df = pd.merge(df1,df_sum, how = 'left', on = 'ID')

# 기준이 2개 이상의 경우
df_sum2 = df2.groupby(by = ['ID', '구매월'])['금액'].sum()
df = pd.merge(df1,df_sum2, how = 'left', on = 'ID')

# 구매월 누락부분을 추가하기
df3 = pd.DataFrame(df_sum2)
# 그룹을 index로 사용하고 싶지 않은 경우에는 as_index = False 설정
df_sum3 = df2.groupby(by = ['ID', '구매월'], as_index = False)['금액'].sum()
df = pd.merge(df1,df_sum3, how = 'left', on = 'ID')

# Quiz 누적 금액과 구매 횟수를 회원 ID별로 구하시오
df = pd.DataFrame({'구매순서' : [1,2,3,4,5], 'ID' : [1,1,2,4,1], '구매월' : [1,1,2,2,3],
                    '금액' : [1000,1500,2000,3000,4000], '수수료' : [100,150,200,300,400]})
df4 = df.groupby(by = ['ID'])['금액'].agg([sum, len])
df4.reset_index(inplace=True)

# Quiz 회원별 최대 사용금액, 최소 사용금액과 최저 수수료의 값을 구하시오
df5 = df.groupby(by = ['ID']).agg({'금액' : [max, min], '수수료' : min}) # dic 구조로 입력함
df5.reset_index(inplace=True)
# 칼럼명 변경하기
df5.columns = ['_'.join(col) for col in df2.columns.values]
print(df5)