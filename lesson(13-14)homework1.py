#Tapsiriq 1.
'''
start_num = int(input('Eded daxil edin: '))
end_num = int(input('Eded daxil edin: '))
for number in range(start_num, end_num ):
    if number % 2 == 1 and not number % 3 == 0 and not number % 5 == 0 and not number % 7 == 0 and not number % 9 == 0:
        print(f'{number} sade ededdir')
else:
    print('')
'''
'''
#Tapsiriq 2.

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j}', end='\t')
    print(end='\n')

#Tapsiriq 3.
start_num = int(input('Eded daxil edin: '))
end_num = int(input('Eded daxil edin: '))
for i in range (start_num, end_num +6):
    for j in range(start_num, end_num +1):
        print(f'{i} * {j}', end='\t')
    print(end='\n')
'''
expression = input('Ededi ifade daxil edin. Meselen (12+23): ')
if '+' in expression:
  num1, num2 = expression.split('+')  # [12, 23]
  sum = int(num1) + int(num2)
  print(f'{num1} + {num2} = {sum}')
elif '-' in expression:
  num1, num2 = expression.split('-')  # [12, 23]
  difference = int(num1) - int(num2)
  print(f'{num1} - {num2} = {difference}')
elif '*' in expression:
  num1, num2 = expression.split('*')  # [12, 23]
  multiplication = int(num1) * int(num2)
  print(f'{num1} * {num2} = {multiplication}')
elif '/' in expression:
  num1, num2 = expression.split('/')  # [12, 23]
  division = int(num1) / int(num2)
  print(f'{num1} / {num2} = {division}')
else:
  print('!!!Düzgün ifade daxil edin!!!')
