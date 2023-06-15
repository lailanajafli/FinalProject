'''

İki siyahıda təsadüfi tam ədədlər var. Siyahıların
ölçüsü eynidir. Aşağıdakıları icra edin:
• Özündə hər iki siyahının elementlərini əks etdirən
üçüncü bir siyahı yaradın;   +
• Özündə hər iki siyahının təkrar olunmayan
elementlərini əks etdirən üçüncü bir siyahı yaradın;
• Özündə hər iki siyahının ümumi elementlərini əks
etdirən üçüncü bir siyahı yaradın;
• Özündə hər iki siyahının yalnız unikal elementlərini
əks etdirən üçüncü bir siyahı yaradın;
• Özündə hər iki siyahının yalnız ən kiçik və ən böyük
elementlərini əks etdirən üçüncü bir siyahı yaradın
'''
import random

list_1 = []
list_2 = []

for i in range(15):
    random_list1 = random.randint(10,100)
    list_1.append(random_list1)
print(list_1)

for j in range(15):
    random_list2 = random.randint(10,100)
    list_2.append(random_list2)
print(list_2)

# 1.

list_3 = list_1 + list_2
print(list_3)

# 2.
list_4 = []
for i in list_1:
    if i not in list_2:
       list_4.append(i)
print(list_4)

# 3.
list_5 = []
for i in list_1:
    if i in list_2:
       list_5.append(i)
print(list_5)

# 4.
list_4 = []
for i in list_1:
    if i not in list_2:
       list_4.append(i)
print(list_4)

# 5.
min = list_3[0]
max = list_3[0]
for i in range(len(list_3)):
    if list_3[i] > max:
        max = list_3[i]
    elif list_3[i] < min:
        min = list_3[i]
print(f'En boyuk eded {max}')
print(f'En kicik eded {min}')




























































































































