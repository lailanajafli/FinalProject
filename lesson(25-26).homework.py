                                #MEN YAZAN 12

# Tapsiriq 1.

outer_list =[[58, 4, 35], [39, 20, 80], [21,56,60]]
total_sum = 0
for inner_list in outer_list:
    for element in inner_list:
        total_sum = total_sum + element
print(total_sum)


# Tapsiriq 2.

import random

outer_list = []
for i in range(3):
    inner_list = []
    for j in range(5):
        random_number = random.randint(-10, 10)
        inner_list.append(random_number)
    outer_list.append(inner_list)
print(outer_list)

for i in range(len(outer_list)):
    for j in range(len(outer_list[i])):
    if outer_list[i][j] < 0:
        outer_list[i][j] = 0
print(outer_list)


# Tapsiriq 3.

import random
outer_list = []
inner_list = []
for i in range(3):
    for j in range(3):
        random_outher_list = random.choice('XO')
        inner_list.append(random_outher_list)
    outer_list.append(inner_list)
for inner_list in outer_list:
    for i in inner_list:
        print(i, end = ' ')
print()

#Tapsiriq 4.

number = [12, 19, 21, 33, 15]

list = []

for i in number:
    inner_list = []
    inner_list = [i, i * i]
    list.append(inner_list)
print(list)
'''

                                                    #mUELLIME YAZAN 

outer_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
sum = 0
for inner_list in outer_list:
    for element in inner_list:
        sum += element
print('Siyahıdakı ededlerin cemi: ', sum)

# Nested listin yaradılması ve mezmununun doldurulması
example_nested_list = [[j*3 for j in range(5)] for i in range(3)]  # -> 3x5 ölçülü siyahı yaradılacaq
print(example_nested_list)
# ========================
example_nested_list_2 = []
for i in range(3):
    for j in range(5):
        example_nested_list_2.append(j)
print(example_nested_list_2)

# Tapşırıq 2
'''
3x5 ölçülü siyahı -10 ile 10 arasındakı random ededler ile doldurulur.
Daha sonra, siyahıdakı bütün mənfi ədədlər 0 ilə əvəz olunur.
'''

import random

outer_list = [[random.randint(-10, 10) for j in range(5)] for i in range(3)]
print(outer_list)

for i in range(len(outer_list)):
    for j in range(len(outer_list[i])):
        if outer_list[i][j] < 0:
            outer_list[i][j] = 0

print(outer_list)

# Tapşırıq 3
'''
X və O hərfləri ile tic-tac-toe lövhəsini təmsil edən iç içə siyahı yaradın.
'''

import random

outer_list = [[random.choice('XO') for j in range(3)] for i in range(3)]

for inner_list in outer_list:
    for element in inner_list:
        print(element, end=' ')
    print()


# Tapşırıq 4
'''
Ədədlərdən ibaret 1-ölçülü siyahı verilmişdir. Meselen: [12, 19, 21, 33, 15]
Hər bir elementin orijinal siyahıdakı müvafiq elementin kvadratı olduğu yeni iç-içə siyahı yaradan kod yazın.
Meselen: [[12, 144], [19, 361], [21, 441], [33, 1089], [15, 225]]
'''

example_list = [12, 19, 21, 33, 15]

nested_list = []

for element in example_list:
    inner_list = [element, element*element]
    nested_list.append(inner_list)

print(nested_list)





























































































































