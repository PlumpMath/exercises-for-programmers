# 간단한 수학

n1 = int(input('What is the first number? '))
n2 = int(input('What is the second number? '))
print(('{} + {} = {}\n' +
       '{} - {} = {}\n' +
       '{} * {} = {}\n' +
       '{} / {} = {}').format(n1, n2, n1 + n2,
                              n1, n2, n1 - n2,
                              n1, n2, n1 * n2,
                              n1, n2, n1 // n2))
