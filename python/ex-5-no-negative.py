# 간단한 수학
# 음수 입력 금지

try:
    n1 = int(input('What is the first number? '))
    if n1 < 0:
        print('No negative value.')
        exit(1)
    n2 = int(input('What is the second number? '))
    if n2 < 0:
        print('No negative value.')
        exit(1)
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
