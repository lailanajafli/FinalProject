#her hansi bir reqemden istediyimiz reqemleri silmek

number = int(input('Eded daxil edin: '))
temp = number
symb = int(input('Silmek istediyiniz reqemi daxil edin: '))
new_num = 0
degree = 1     # ededin mertebesi
while number > 0:
    digit = number % 10
    if digit != symb:
        new_num = new_num + digit * degree
        degree = degree * 10
    number = number // 10
print(f'Old number is {temp}')
print(f'New number is {new_num}')

'''
# Mesele. İstifadeçi klaviaturadan 6 reqemli eded daxil edir.
# Bu ededin şanslı olub olmadığını yoxlayan proqram yazın.
# Şanlslı eded o eded sayılır ki, ededin ilk 3 reqeminin cemi 2-ci 3 reqeminin cemine beraber olsun.
# Meselen 123321 ededi şanslıdır. 1+2+3 = 3+2+1

number = int(input('Eded daxil edin: '))
temp = number
count = 0
sum1 = 0
sum2 = 0
while number > 0:
    digit = number % 10
    count += 1
    if count <= 3:                  # count <= len(str(number)) / 2
        sum1 = sum1 + digit
    else:
        sum2 = sum2 + digit
    number = number // 10

if sum1 == sum2:
    print(f'{temp} ededi şanslı ededdir')
else:
    print(f'{temp} ededi şanslı eded deyil')

#Mesele. Yuxarıdakı meseleni istifadeçi 6 reqemli eded daxil edene geder
# ededi tekrar teleb etmesini temin edin.


while True:
    number = int(input('Eded daxil edin: '))
    if len(str(number)) == 6:
        break

temp = number
count = 0
sum1 = 0
sum2 = 0
while number > 0:
    digit = number % 10
    count += 1
    if count <= 3:                  # count <= len(str(number)) / 2
        sum1 = sum1 + digit
    else:
        sum2 = sum2 + digit
    number = number // 10

if sum1 == sum2:
    print(f'{temp} ededi şanslı ededdir')
else:
    print(f'{temp} ededi şanslı eded deyil')


# Aşağıdakı kodun neticesi ne olacaq?

a = 0
for i in 'Hakuna Matata':
    a += int(bool(i))
print(a)

# Sual2
# Aşağıdakı dövr neçe defe icra olunacaq?

for i in range(15):      # 15 * 4
    for j in range(4):
        print('Hello World!')


# Dövrler. Task 1
# 1-den 9-a geder vurma cedvelini öz formatı ile ekrana çap edin.

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} * {j}', end='\t')
    print(end='\n')

# Task 2. Ekrana aşağıdakı görüntü çap olunsun:

1 1 1 1 1 
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
1 1 1 1 1


for i in range(5):
    for j in range(5):
        print((i + 1) % 2, end='\t')
    print()


# Task 3. Ekrana aşağıdakı görüntü çap olunsun:

1 0 1 0 1 
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 1

for i in range(5):
    for j in range(5):
        print((j + 1) % 2, end='\t')
    print()

# Task 4. Ekrana aşağıdakı görüntü çap olunsun:

1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end='\t')
    print()
'''
# Task 5. Ekrana aşağıdakı görüntü çap olunsun:
'''
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1

for i in range(5, 0, -1):
    for j in range(5, 0, -1):
        print(i, end='\t')
    print()
'''

# chr() ve ord() funksiyaları
# print(chr(65))  # chr() - kodu simvola çevirir
# print(ord('A')) # ord() - simvolun eded qarşılığını qaytarır
# ASCII = American Standart for Code Information Interchange
# ASCII table simvolların ededlere uyğunlaşdırılması üçün olan cedveldir
# Task 6. Ekrana aşağıdakı görüntü çap olunsun:
# '''
# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E
#
'''
for i in range(5):
    for j in range(5):
        print(chr(65 + i), end='\t')
    print()
'''
# Task 7. Ekrana aşağıdakı görüntü çap olunsun:
'''
* 
* * 
* * *
* * * * 
* * * * *
'''
'''
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end='\t')
        else:
            print(end='\t')
    print()
print()
print()
'''
# Task 8. Ekrana aşağıdakı görüntü çap olunsun:
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
'''
for i in range(5):
    for j in range(5):
        if j >= i:
            print('*', end='\t')
        else:
            print(end='\t')
    print()
'''
# Task 9. Ekrana aşağıdakı görüntü çap olunsun:
'''
        *
      * * 
    * * *
  * * * * 
* * * * * 
'''

# Task 10. Ekrana aşağıdakı görüntü çap olunsun:
'''
* * * * *
* * * *
* * * 
* * 
*
'''
'''
for i in range(5):
    for j in range(5):
        if j + i <= 4:
            print('*', end='\t')
        else:
            print(end='\t')
    print()
'''
# Task 11. Ekrana aşağıdakı görüntü çap olunsun:
'''
* * * * *
  * * * 
    * 

for i in range(5):
    for j in range(5):
        if j >= i and j + i <= 4:
            print('*', end='\t')
        else:
            print(end='\t')
    print()

# Task 12. Ekrana aşağıdakı görüntü çap olunsun:

    * 
  * * * 
* * * * *



# Task 13. Ekrana aşağıdakı görüntü çap olunsun:

* 
* * 
* * *
* * 
* 
'''

# Task 14. Ekrana aşağıdakı görüntü çap olunsun:
'''
        *
      * *
    * * *
      * *
        *
'''
