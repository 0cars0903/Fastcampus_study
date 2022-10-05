import pandas as pd
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/과일가게.csv')
# 경로 복사 하여 붙여 넣기
df.head() # 처음부터 5행까지 출력
df.tail() # 뒤에서부터 5행까지 출력

# 첫번째 열을 인덱스열로 삼고 싶을 경우
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/과일가게.csv', index_col=0)
# print(df.head())

# 구분자가 ,가 아닌 다른 문자인 경우(sep=)
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/read_sep.txt', 
                index_col=0, sep = '|')
# print(df.head())

# 헤더가 여러줄인 경우
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/read_multi_header.csv', 
                header=1)
# print(df.head())

# 데이터를 읽으면서 칼럼명을 추가할 경우
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/make_column_name.csv', 
                index_col=0, names=['품목', '크기', '금액', '수수료'])
# print(df.head())

# 원하는 칼럼만 사용하고 싶을 때
df = pd.read_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/과일가게.csv', 
                usecols=['품목', '크기'])
# print(df.head())

# 파일저장 방법
df.to_csv('C:/Users/heesj/OneDrive/바탕 화면/Github/Fastcampus_study/Fastcampus_study_step2/make1.csv')