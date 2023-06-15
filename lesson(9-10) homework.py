#Tapsiriq 1.
start_number = int(input('Eded daxil edin: ')) #20
end_number = int(input('Eded daxil edin: ')) #41

for i in range(start_number, end_number):
    for j in range(start_number, end_number):
        print('*', end='\t')
    print()

#Tapsiriq 2.

#1.
start_number = int(input('Eded daxil edin: ')) #20
end_number = int(input('Eded daxil edin: ')) #41

for number in range(start_number, end_number):
    print(number, end = '\t')

for number in range(start_number, end_number):
    if number % 7 == 0:
        print(f' \n {number}')

for number in range(end_number, start_number, -1):
    print(f' {number}', end = ' ')

for number in range(start_number, end_number):
    if number % 5 == 0:
        print(f' \n {number}')


#Tapsiriq 3.

start_num = int(input('Eded daxil edin: '))
end_num = int(input('Eded daxil edin: '))
for number in range(start_number, end_number +1):
    if number % 3 == 0 and number % 5 == 0:
        print('Fizz Buzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)

#2.
start_num = int(input('Eded daxil edin: '))
end_num = int(input('Eded daxil edin: '))
while start_num < end_num:
    if start_num % 5 == 0:
        print(start_num)
    start_num = start_num + 1
print('Buzz')

#3.
start_num = int(input('Eded daxil edin: '))
end_num = int(input('Eded daxil edin: '))
while start_num < end_num:
    if start_num % 3 == 0 and start_num % 5 == 0:
        print(start_num)
    start_num = start_num + 1

