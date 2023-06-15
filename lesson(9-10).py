#Dovrler
# Dovrler - hereketle

# 1- den 10-a qeder ededleri cap etmek
'''
number = 1
while number < 10:
    print(number)
    number = number + 1 # number += 1

# Tapşırıq 1
start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
while start < end:
    print(start)
    start = start + 1

#Tapsiriq 2.

start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
while end > start:
    print(end)
    end = end - 1 # end -= 1
'''

#Tapsiriq 3.

start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
while start < end:
    if start % 2 == 0:          #buradaki 0 i 1 elesek tekleri tapmis olariq
        print(start)
    start = start + 1
'''
#Tapsiriq 4.

start = int(input('Eded daxil edin: '))
end = int(input('Eded daxil edin: '))
sum = 0
while start < end:
    if start % 3 == 0 and start % 5 == 0:
        sum = sum + start
        print(start)
    start = start + 1
print(sum)

#Tapşırıq 5
# Faktorial — 7! = 7 * 6 * 5 * 4 * 3 * 2 * 1
number = int(input('Enter number: ')) # 7
factorial = 1
while number > 0:
    factorial = factorial * number
    number = number - 1
    print(f'Faktorial deyeri: {factorial}')
print('the end')

#Tapsiriq 6.

#Tapşırıq 6
number = int(input('Eded daxil edin: ')) #234 // 10
count = 0
sum = 0
while number > 0:
    digit = number % 10
    number //= 10
    sum = sum + digit
    count += 1
print(f'Reqemlerin sayı: {count}')
print(f'Reqemlerin cemi: {sum}')


# Sonsuz dovr sintaksisi
#Idareetme operatorlari - break
while True:
    user_input = input('Secim daxil eidn: ')
    if user_input == '1' :
        break

#Idareetme operatoru - continue
start_number = int(input('Eded daxil edin: '))
end_number = int(input('Eded daxil edin: '))
while start_number < end_number:
    start_number += 1                    #hnghgjjfckghmgkjcghjgfvgbnhbv
    if start_number % 2 == 1:
        continue
    print(start_number)

# For dövrü

for keyword in 1,2,3,4,-5,10,45,234:
    print(keyword)

for keyword in 'IT Step Academy':
    print(keyword)


# range() funksiyası 3 arqument qebul eded bilir
# 1 arqument ile
#range(20)   # 0-dan 20-ye qeder, 20 daxil olmamaqla
#range(5, 20) # 5-den başlayır 20-ye geder, 20 daxil olmamaqla
#range(5, 20, 3) # 5, 8, 11, 14, 17 ...

print(list(range(20)))
print(list(range(5, 20)))
print(list(range(5, 20, 3)))
print(list(range(20, 5, -1)))

for element in range(30, 100):
    if element % 2 == 1:
        continue
    print(element)

# Tapşırıq: for ile istifadeçinin daxil etdiyi diapazonda 7-ye bölünen
# ededleri çap edin
start_number = int(input('Eded daxil edin: '))
end_number = int(input('Eded daxil edin: '))
for i in range(start_number, end_number):
    if i % 7 == 0:
        print(i)


# İç içe konstruksiyalar. Nested if

# *******
for i in range(5):  #1
    for j in range(7): #1
        print('*', end='\t') #0,1,2,3,4,5,6
    print()


for i in range(1, 10):
    for j in range(1, 10):
        print(j*i, end='\t')
    print(),

# Dördbucaqlı çap edin
for i in range(1, 10):
    for j in range(1, 10):
        if i == 1 or i == 9 or j == 1 or j == 9:
            print(j, end='\t')
        else:
            print(end='\t')
    print()


# X-vari çap edin
for i in range(1, 10):
    for j in range(1, 10):
        if i == j or i + j == 10 or i == 1 or i == 9 or j == 1 or j == 9:
            print(j, end='\t')
        else:
            print(end='\t')
    print()
'''














