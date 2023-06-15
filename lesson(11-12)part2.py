#Tapsiriq 1.

x = int(input('Eded daxil edin: '))
y = int(input('Eded daxil edin: '))
print(pow(x,y))

#Tapsiriq 2.

count = 0
for i in range(100, 1000):
    digit1 = i // 100
    digit2 = i // 10 % 10
    digit3 = i % 10
    if digit1 == digit2 or digit1 == digit3 or digit2 == digit3:
        count += 1
print(f'Iki eyni rəqəmə malik tam ədədlərin sayı: {count}')


#Tapsiriq 3.

count = 0
for i in range(1000, 10000):    # 8486
    digit1 = i // 1000
    digit2 = i // 100 % 10
    digit3 = i // 10 % 10
    digit4 = i % 10
    if digit1 != digit2 and digit1 != digit3 and digit1 != digit4 and digit2 != digit3 and digit2 != digit4 and digit3 != digit4:
        count += 1
print(f'Reqemleri fərqli olan tam ədədlərin sayı: {count}')

#Tapsiriq 4.
number = int(input('Eded daxil edin: '))
temp = number
new_num = 0
degree = 1
while number > 0:
    digit = number % 10
    if digit != 3 and digit != 6:
        new_num = new_num + digit * degree
        degree = degree * 10
    number = number // 10
print(f'Old number is {temp}')
print(f'New number is {new_num}')









