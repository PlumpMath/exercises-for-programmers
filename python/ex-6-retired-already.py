# 퇴직 계산기

import datetime

current_age = int(input('What is yout current age? '))
retire_age = int(input('At what age would you like to retire? '))
left_years = retire_age - current_age
current_year = datetime.date.today().year
retire_year = current_year + left_years

if (left_years < 0):
    print('You should have retired already.')
else:
    print('You have ' + str(left_years) + ' years left until you can retire.')
    print('It\'s ' + str(current_year) + ', ' +
          'so you can retire in ' + str(retire_year) + '.')

