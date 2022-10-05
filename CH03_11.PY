import pandas as pd
df = pd.DataFrame({'a' : [1,2,3,4,5]})

# Quiz a 가 2보다 작으면 '2미만', 4보다 작으면 '4미만', 4보다 크면 '4이상'이 저장된 b칼럼을 추가하시오

# b칼럼 추가
df['b'] = 0

# 조건에 맞는 데이터 프레임 제작
a = df[df['a'] < 2] # a = [1,0]
b = df[(df['a'] >= 2)& (df['a'] < 4)]
c = df[df['a'] >= 4]

# b 칼럼에 문자열 입력
df['b'][a.index] = '2미만'
df['b'][b.index] = '4미만'
df['b'][c.index] = '4이상'

# print(df)

# 함수와 apply를 이용하여 간단화 하기
def case_function1(x):
    if x <2:
        return '2미만'
    elif x < 4:
        return '4미만'
    else:
        return '4이상'
df['c'] = df['a'].apply(case_function1)

# Quiz 1 'one' 2 'two' 3 'three' 4 'four' 5 'five' 출력
def case_function2(x):
    if x == 1:
        return 'one'
    elif x == 2:
        return 'two'
    elif x == 3:
        return 'three'        
    elif x == 4:
        return 'four'
    elif x == 5:
        return 'five'
df['d'] = df['a'].apply(case_function2)

# map을 이용할 경우
a = {1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five'}
df['e'] = df['a'].map(a)
print(df)