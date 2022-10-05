import pandas as pd
df = pd.DataFrame({'판매일' : ['5/11/21','5/12/21','5/13/21','5/14/24','5/15/21'],
                   '판매량' : ['10','15','20','25','30'], 
                   '방문자수' : ['10','-','17','23','25'],
                   '기온' : ['24.1','24.3','24.8','25','25.4']})

# type 확인
df.dtypes

# 판매량 보정 열 추가
df.astype({'판매량' : 'int'}) # type 변환
df = df.astype({'판매량' : 'int'})
df['판매량 보정'] = df['판매량'] + 1 

# 방문자수 tpye 변환(공백이 존재할 경우)
df['방문자수'] = pd.to_numeric(df['방문자수'], errors='coerce') # 오류 발생 시, nan으로 대체

# NaN 값을 변환하여 int형태로 변환하기
df.fillna(0, inplace=True)
df = df.astype({'방문자수' : int})

# 판매일의 datetime 형태로 변경
df['판매일'] = pd.to_datetime(df['판매일'], format="%m/%d/%y")
print(df)