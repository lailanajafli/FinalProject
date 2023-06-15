# Lists - Siyahılar
# Siyahılar -> müxtelif tipli elementler toplusudur (collection).
'''
list_1 = []
list_2 = list()
print(type(list_1))
print(type(list_2))
'''

# List-in doldurulması:
'''
list_1 = [23, 12, 56, 78]
list_2 = list('Hello World')  #list() funksiyası cemi 1 arqument qebul edir, ve bu deyer iterable olmalıdır. (yeni tekrarlanan)
print(list_1)
print(list_2)
'''

# Listler -> müxtelif tipli elementler toplusudur.
'''
elements = [23, 14, 3.5, 'Bob', 'Alice', True, False]
print(elements)
'''
'''
# List-lerde indexlenme (sıralanma)
         #   0   1    2     3      4      5      6
elements = [23, 14, 3.5, 'Bob', 'Alice', True, False]
         # - 7   6    5    4       3       2      1

print(elements[4])
print(elements[-2])
'''

# Listlerde elementler ayrı ayrı deyişenler arasında paylana biler.
'''
expression = '12+34'
print(expression.split('+'))  # [12, 34]
num1, num2, str3, str4 = [12, 34, 'Tom', 'Bob']
print(num1, ' ', num2, ' ', str3, ' ', str4)
# QEYD: deyişenlerin ve elementlerin sayı eyni olmalıdır
'''

# List Slicing -> bire bir setirler ile eynidir
'''
elements = [23, 14, 3.5, 'Bob', 'Alice', True, False]
print(elements[::2])
print(elements[::-1])
'''

# Listin elementlerine index-e göre müraciet - 2
'''
elements = [23, 14, 3.5, 'Bob', 'Alice', True, False]
print(elements[3][0])
'''
# List-in elementlerinin çap olunması:
'''
elements = [23, 14, 3.5, 'Bob', 'Alice', True, False]
for i in elements:
    print(i)
'''

# Tasklar - 1
# Task 1. Bir list teyin edin (numbers) ve listi tam ededler ile doldurun.
# Bu elementleri yan yana çap edin.
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]

for i in numbers:
    print(i, end=' ')
'''
# Task 2. Bu elementlerin cemini tapın.
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
total_sum = 0
for i in numbers:
    total_sum = total_sum + i
print(total_sum)
'''

# Task 3. Bu elementlerin ededi ortasını tapın.
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
total_sum = 0
count = 0
for i in numbers:
    total_sum = total_sum + i
    count = count + 1
print(total_sum / count)
print(total_sum / len(numbers))  # count = len(numbers)
'''
# Task 4. Bu ededlerden cüt olanların cemini, tek olanların hasilini tapın.
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
total_sum = 0
multiplication = 1
for i in numbers:
    if i % 2 == 0:
        total_sum += i
    else:
        multiplication *= i
print('Cüt ededlerin cemi', total_sum)
print('Tek ededlerin hasili', multiplication)
'''

# Task 5. İndex-i cüt olan elementlerin hasilini tapın.
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
multiplication = 1
for i in range(len(numbers)):    # range(8)
    if i % 2 == 0:
        multiplication *= numbers[i]
print(numbers)
print('İndeksi cüt olan elementlerin hasili: ', multiplication)
'''


# List üzerinde iş: + ve *.
# Setirler ile oxşardır
'''
list_1 = [1, 2, 3]
list_2 = [-1, 5, 6]
print(list_1 + list_2)
print(list_1 * 6)
'''

# List functions:
'''
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
print(sum(numbers))
print(len(numbers))
print(max(numbers))
print(min(numbers))
'''


# List methods
# Qeyd: listin metodları listin üzerinde işleyir.
# Yeni, orijinal list deyişir.

# .count() metodu -> verilmiş elementin list-de neçe defe
# rast geldiyini sayır
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
print(names.count('Bob'))
'''
# Listlerde axtarış üçün var: .index() ve IN ve NOT IN açar sözleri.
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
# print(names[9])    # IndexErrror
print(names.index('Bob'))
# print(names.index('Marley'))  # ValueError

if 'Bob' in names:
    print('Yes')
if 'Marley' not in names:
    print('No')
'''

# Elementlerin silinmesi: .pop(), .remove(), .clear(), del açar sözü
# .pop() -> verilmiş index-deki elementi silir,
# arqument verilmedikde sonuncu elementi silir
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.pop()
print(names)

names.pop(2)
print(names)
'''
# Qeyd: .pop() metodu sildiyi deyeri bize qaytarır
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
deleted_variable = names.pop(1)
print(deleted_variable)
print(names)
'''

# .remove() metodu -> verilmiş elementi silir
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.remove('Anna')  #ValueError
print(names)
'''

# .clear() metodu -> verilmiş listi 0-layır
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.clear()
print(names)
'''

# del açar sözü -> deyişeni ram üzerinden silir
'''
variable = 89
del variable
print(variable)

names = ['Bob', 'Alice', 'Tom', 'Bob']
del names
print(names)

names = ['Bob', 'Alice', 'Tom', 'Bob']
del names[3]
print(names)
'''

# Elementlerin elave olunması: .append(), .insert()
# .append() metodu -> listin sonuna verilmiş elementi elave edir
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.append('Anna')
print(names)
names.append(True)
print(names)

# .insert() metodu -> verilmiş index-e verilmiş elementi elave edir
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.insert(0, 'Anna')
names.insert(2, True)
print(names)
'''

# Elementlerin sıralanması: .reverse(), .sort(), .sort(reverse = True)
'''
names = ['Bob', 'Alice', 'Tom', 'Bob']
names.reverse()  # -> elementlerin sıralanmasını tersine çevirir
print(names)
'''

# .sort() metodu -> elementleri artan qaydada düzür.
# Qeyd: listin elementleri eyni tipli olmalıdır
'''
names = ['Bob', 'Alice', 'Tom', 'Bob', 34]  # TypeError
names.sort()
print(names)

numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
numbers.sort()
print(numbers)

# .sort(reverse = True) -> azalan qaydada elementleri sıralayır
numbers = [23, 34, -56, 78, -100, 0, 111, 89, 60]
numbers.sort(reverse=True)
print(numbers)
'''

# Example: Boş listin mezmununu 0 ile 100 arasında random 10 eded ile doldurun.
'''
import random

numbers = []

for i in range(10):
    random_number = random.randint(0, 101)
    numbers.append(random_number)

print(numbers)
'''

# Tasklar - 2
# Task1: Boş listi istifadeçinin daxil etdiyi aralıqda,
# istifadeçinin daxil etdiyi say qeder random tam ededler ile doldurun.
'''
import random

numbers = []
start = int(input('Start ededini daxil edin: '))
end = int(input('End ededini daxil edin: '))
amount = int(input('Element sayını daxil edin: '))

for i in range(amount):
    random_number = random.randint(start, end+1)
    numbers.append(random_number)

print(numbers)
'''

# Boş listi doldurun ve en böyük elementini tapın.
# Heç bir metoddan istifade etmeden.
'''
import random

numbers = []
start = int(input('Start ededini daxil edin: '))
end = int(input('End ededini daxil edin: '))
amount = int(input('Element sayını daxil edin: '))

maximum = 0
count = 0

for i in range(amount):
    random_number = random.randint(start, end+1)
    numbers.append(random_number)
    count += 1
    if count == 1:
        maximum = random_number
    if maximum < random_number:
        maximum = random_number

print(numbers)
print('Maximum is: ', maximum)
'''

# Boş listi doldurun ve listin en kiçik elementini tapın.
'''
import random

numbers = []
start = int(input('Start ededini daxil edin: '))
end = int(input('End ededini daxil edin: '))
amount = int(input('Element sayını daxil edin: '))

minimum = 0
count = 0

for i in range(amount):
    random_number = random.randint(start, end+1)  # verilmiş aralıqda tesadüfi element yaradılır
    numbers.append(random_number)
    count += 1
    if count == 1:
        minimum = random_number
    if minimum > random_number:
        minimum = random_number

print(numbers)
print('Minimum is: ', minimum)
'''

# Yol - 2
'''
import random

numbers = []
start = int(input('Start ededini daxil edin: '))
end = int(input('End ededini daxil edin: '))
amount = int(input('Element sayını daxil edin: '))


# siyahının tesadüfi ededler ile doldurulması
for i in range(amount):
    random_number = random.randint(start, end+1)  # verilmiş aralıqda tesadüfi element yaradılır
    numbers.append(random_number)

maximum = numbers[0]     # [23, -4, 56, 78, 9]
for i in numbers:
    if i > maximum:
        maximum = i

print(numbers)
print('Maximum is: ', maximum)




'''

'''
# Boş listi 10 eded random 2-ye, 3-e ve 8-e
# eyni anda bölüne bilen ededler ile doldurun.

import random

numbers = []
# count = 0

while len(numbers) <= 10:
    random_number = random.randint(0, 200)
    if random_number % 2 == 0 and random_number % 3 == 0 and random_number % 8 == 0:
        numbers.append(random_number)
        #count += 1

print(numbers)
'''