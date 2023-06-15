# Tapsiriq 1.

expression = input('Ededi ifade daxil edin: ')
if '+' in expression:
    num1, num2 = expression.split('+')
    sum = int(num1) + int(num2)
    print(f'{num1} + {num2} = {sum}')
elif '-' in expression:
    num1, num2 = expression.split('-')
    difference = int(num1) - int(num2)
    print(f'{num1} - {num2} = {difference}')
elif '*' in expression:
    num1, num2 = expression.split('*')
    multiplication = int(num1) * int(num2)
    print(f'{num1} * {num2} = {multiplication}')
elif '/' in expression:
    num1, num2 = expression.split('/')
    division = int(num1) / int(num2)
    print(f'{num1} / {num2} = {division}')
else:
    print('!Düzgün ifade daxil edin!')

# Tapsiriq 2.

max = 0
min = 0
neg_count = 0
pos_count = 0
zero_count = 0
count = 0
string_of_integers += str(random_number) + ' '

for i in range(20)
    random_number = random.randint(-80, 101)
    string_of_integers += str(random_number) + ' '
    count += 1
    if count == 1:
        max = random_number
        min = random_number
    if random_number > max:
        max = random_number
    if random_number < max:
        max = random_number
    if random_number > 0:
        pos_count += 1
    elif random_number < 0:
        neg_count += 1
    else
        zero_count += 1

print(string_of_integers)
print(f'Minimum is {min}')
print(f'Minimum is {max}')
print(f'Zero numbers count is {zero_count}')
print(f'Positive numbers count is {pos_count}')
print(f'Negative numbers count is {neg_count}')




































