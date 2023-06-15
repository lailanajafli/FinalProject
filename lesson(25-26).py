for i in range(length):
    j = random.randint(i, length-1)     # tesadüfi index yaradılır
    # swap xüsusiyyeti
    original_list[i], original_list[j] = original_list[j], original_list[i]

print(original_list)


# random kştabxanasının .shuffle() metodu -> arqument olaraq list qebul edir, listin özünü deyişir
# ve neticede qarışdırılmış list elde edirik
# shuffle = qarışdırmaq
random.shuffle(original_list)

print(original_list)




# Keçen ders verilen tapşırıqlar:
# list-den terkibinde 0 reqemi olan elementlerin silinmesi
numbers = [12, 32, 21, 202, 40, 50]

for i in range(len(numbers)):
    number = numbers[i]
    degree = 1
    new_num = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit != 0:
            new_num = new_num + digit * degree
            degree *= 10
            numbers[i] = new_num
print(numbers)

# İstifadeçiden sözlerin siyahısını götüren ve polindrom olan bütün
# elementleri çapa veren proqram yazın


# Ededler siyahısında en kiçik iki elementi çap eden proqram
numbers = [12, 32, 21, 202, 40, 50]
first_min = min(numbers)  # 1-ci en kiçik elementi verer
print(first_min)
numbers.remove(first_min)
second_min = min(numbers)
print(second_min)

# Siyahıdakı bütün dublikat elementleri çap eden proqram



# Listin daxilindeki elementin deyerinin deyişmesi
numbers = [12, 32, 21, 202, 40, 50, 32, 32, 32]    # 32 -> 11

numbers[1] = 11  # listdeki elementi deyişir

# Yanlış: listdeki element deyişmir
for element in numbers:
    if element == 32:
        element = 11
print(numbers)


# Doğru: listdeki element deyişir
for index in range(len(numbers)):
    if numbers[index] == 32:
        numbers[index] = 11
print(numbers)




# listin mezmununun doldurulması: variant 3, 4

# variant 3. Syntax

numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)

numbers_2 = [i for i in range(5)]
print(numbers_2)

numbers_3 = [i*i for i in range(5, 10)]
print(numbers_3)

import random
numbers_4 = [random.randint(10, 100) for i in range(10)]
print(numbers_4)



# variant 4
# Listin daxilinde input() funksiyasını çağıra bilirik

names = [input('Ad1 daxil edin: '), input('Ad2 daxil edin: '), input('Ad3 daxil edin: ')]
print(names)

# Nested lists. (İç içe siyahılar)
                                                    #inner list
total_list = [12, 34, 12.5, 'Easjdh', True, False, [12, 23, 34]]
print(total_list)
print(total_list[6])

print(total_list[6][1])

# Nested siyahılar nedir?
# Biz bilirik ki, siyahı müxtelif tipli elementler toplusudur.
# ve bu tiplere listlerin özü de daxildir

nested_list = [[1.2, 1.3, 1.4], [2.3, 2.5], [3.6, 3.7], [4.0, 4.2]]

# Tebii ki bütün list metodları daxili listlere tetbiq oluna biler
nested_list[1].append(2.4)
print(nested_list)

nested_list[1].insert(1, 2.4)
print(nested_list)

nested_list[0].pop(0)
print(nested_list)

# .clear() metodu
nested_list[2].clear()
print(nested_list)


nested_list = [1, 2, 3, [3.3, 3.4, [3.44, 3.45]]]
print(nested_list[3][2][0])

# İç içe listlerin yaradılması ve mezmunun doldurulması

# Example: 3x2 ölçülü bir siyahı yaradılsın ve tesadüfi ededler ile doldurulsun

student_1 = ['Ad1', 'Soyad1']
student_2 = ['Ad2', 'Soyad2']

# variant 1
all_students = []
all_students.append(student_1)
all_students.append(student_2)
print(all_students)

# variant 2 -> eyni neticeni verir
all_students = [['Ad1', 'Soyad1'], ['Ad2', 'Soyad2']]
print(all_students)

# 3x2 ölçülü bir siyahı yaradılsın ve tesadüfi ededler ile doldurulsun
# Netice: [ [], [], [] ]
import random

outer_list = []

for i in range(3):
    inner_list = []
    for j in range(2):
        random_number = random.randint(0, 10)
        inner_list.append(random_number)
    outer_list.append(inner_list)

print(outer_list)

# Tapşırıq:
# 2x3 ölçülü nested list yaradın. Listin elementlerini istifadeçi özü daxil etsin.

outer_list = []

for i in range(2):
    inner_list = []
    for j in range(3):
        user_input = int(input('Element daxil edin: '))
        inner_list.append(user_input)
    outer_list.append(inner_list)

print(outer_list)

# İç içe listin elementlerinin çap olunması:
# Elementler ile çap
for inner_list in outer_list:
    for element in inner_list:
        print(element)


# İndeksler ile çap
for i in range(len(outer_list)):
    for j in range(len(outer_list[i])):
        print(outer_list[i][j])

# Tapşırıqlar - 1

names = [['Bob', 'Michele'], ['Alice', 'Tom'], ['Fred', 'David']]

# 'Samantha' ile 'Frank' adlarını bir element kimi listin sonuna elave edin.
add_list = ['Samantha', 'Frank']
names.append(add_list)

# 'Ted' adını listin 1-ci elementinin sonuna elave edin.
names[0].append('Ted')
print(names)

# 'Mary' adını listin 2-ci elementinin evveline elave edin.
names[1].insert(0, 'Mary')
print(names)

# 'Fred' adını listden silin.
names[2].remove('Fred')
print(names)

# 'Cindy' adı listin bir elementidir? Bes 'Samantha'?
for inner_list in names:
    if 'Cindy' in inner_list:
        print('Cindy listin elementidir')
    if 'Samantha' in inner_list:
        print('Samantha listin elementidir')


# names listindeki daxili listlerin elementlerini eks qaydada düzün.
for inner_list in names:
    inner_list.reverse()
print(names)

# names listindeki daxili listlerin elementlerini alfabetik olaraq sıralayın.
for inner_list in names:
    inner_list.sort()
print(names)

# Tapşırıqlar - 2

'''
3x3 ölçülərinde iç içə siyahı yaradın. Siyahını 1 ilə 100 arasında təsadüfi tam ədədlərlə doldurun.
'''

import random

outer_list = []

for i in range(3):
    inner_list = []
    for j in range(3):
        random_number = random.randint(1, 100)
        inner_list.append(random_number)
    outer_list.append(inner_list)

print(outer_list)

'''
İstenilen ölçülü iç içe siyahıdakı hər bir elementi ayrıca sətirdə çap edən kod yazın.
'''
outer_list = [[58, 4, 35], [39, 20, 80], [21, 56, 60]]

for inner_list in outer_list:
    for element in inner_list:
        print(element)


'''
İç içe siyahıdakı hər bir elementi yan yana sətirdə çap edən kodu yazın.
'''
outer_list = [[58, 4, 35], [39, 20, 80], [21, 56, 60]]

for inner_list in outer_list:
    for element in inner_list:
        print(element, end=' ')

İç içe siyahıdakı hər bir daxili listin elementlerini ayrıca sətirdə çap edən kodu yazın.
'''
outer_list = [[58, 4, 35], [39, 20, 80], [21, 56, 60]]

for inner_list in outer_list:
    for element in inner_list:
        print(element, end=' ')
    print()




































































































