# 글자 수 세기
# 입력 없을 때 메시지 출력

user_input = input('What is the input string? ')

if user_input:
    print(user_input + ' has ' + str(len(user_input)) + ' characters.')
else:
    print('Please input something.')
