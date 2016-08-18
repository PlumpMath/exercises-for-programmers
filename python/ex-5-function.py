# 간단한 수학
# 계산 부분을 함수로 구현

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


def calc(n1, n2):
    return [n1 + n2, n1 - n2, n1 * n2, n1 // n2]

result = calc(n1, n2)

print(('{} + {} = {}\n' +
       '{} - {} = {}\n' +
       '{} * {} = {}\n' +
       '{} / {} = {}').format(n1, n2, result[0],
                              n1, n2, result[1],
                              n1, n2, result[2],
                              n1, n2, result[3]))
