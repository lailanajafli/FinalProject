names = ['Bob', 'Michele', 'Alice', 'Tom', 'Fred', 'David']
birth_years = [1990, 1992, 1995, 1996, 1989, 1988]

# 1.
'''
names.append('Samantha')
print(names)
'''

# 2.
'''
names.insert(0, 'Ted')
print(names)
'''
# 3.
'''
names.pop(5)
print(names)
'''
# 4.
'''
if 'Cindy' in names:
    print('Yes')
if 'Cindy' not in names:
    print('No')
'''
# 5.
'''
print(names[::-1])
'''
# 6.
'''
names.sort()
print(names)
'''

# 7.
'''
birth_years.sort(reverse=True)
print(birth_years)
'''
# 8.
'''
string = 'Iphone X, Iphone XR, Iphone XS'
list = []
list_1 = string.split(', ')
print(list_1)

# 9.
print(max(birth_years))
print(min(birth_years))


# 10.
print(birth_years.count(1990))

# 11.
birth_years.clear()
print(birth_years)

# 12.
list_1 = input(' 1-ci Marka adi elave edin: ')
list_2 = input(' 2-ci Marka adi elave edin: ')
list_3 = input(' 3-cu Marka adi elave edin: ')
list_4 = []
list_4 = list_1 + list_2 + list_3
print(list( list_4))

# 13.
import random

list_1 = []
negative = 0
cut = 0
tek = 0
index_3 = 1
product = 1
for i in range(20):
    random_numbers = random.randint(-100, 100)
    list_1.append(random_numbers)
print(list_1)
for i in list_1:
    if i < 0:
        negative += i
    if i % 2 == 0:
        cut += i
    if i % 2 == 1:
        tek += i
    if list_1.index(i) % 3 == 0:
        index_3 *= i
print(negative)
print(cut)
print(tek)
print(index_3)
'''

#Tapsiriq

'''
number = [ 90, 86, 13, 100, 52, 40]
for i in number:
    if i == 0:
        number.remove(5)
        print(number)
'''
'''
user = input('Soz daxil edin:')
if user == user[::-1]:
    print(list(f'{user} polindromdur'))
else:
    print(list(user))
'''
import random

numbers = []
numbers = int(input('Start ededini daxil edin: '))

for i in range:
    random_number = random.randint(0, 100)
    numbers.append(random_number)
    print(max(numbers))
    print(min(numbers))

# 1
import random
numbers = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)
for el in list:
    for a in str(el):
        if a == '0':
            list.remove(el)
print(list)
# 2
words = input('Sozler elave edin: ')
word_list = words.split(', ')
for i in word_list:
    if i.upper() == i[::-1].upper():
        word_list.remove(i)
print(word_list)
# 3
import random
list = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)

minimum = list[0]
for j in list:
    if j < minimum:
        minimum = j
list2 = list.remove(minimum)
minimum2 = list2[0]
for a in list2:
    if a < minimum2:
        minimum2 = a
print(minimum + minimum2)
# 4
import random
list = []
dublikat = []
for i in range(10):
    random_numbers = random.randint(-100, 100)
    list.append(random_numbers)
print(list)
for j in list:
    if list.count(j) != 1:
        dublikat.append(j)
print(dublikat)





































































