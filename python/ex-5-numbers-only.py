# 간단한 수학
# 숫자만 입력

try:
    n1 = int(input('What is the first number? '))
    n2 = int(input('What is the second number? '))
except ValueError:
    print('Numbers only.')
    exit(1)

print(('{} + {} = {}\n' +
       '{} - {} = {}\n' +
       '{} * {} = {}\n' +
       '{} / {} = {}').format(n1, n2, n1 + n2,
                              n1, n2, n1 - n2,
                              n1, n2, n1 * n2,
                              n1, n2, n1 // n2))
