# 글자 수 세기
# 기본 버전

user_input = input('What is the input string? ')

if user_input:
    print(user_input + ' has ' + str(len(user_input)) + ' characters.')
else:
    print('Please input something.')
