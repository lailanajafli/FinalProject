'''
Tapşırıq 1
Tam ədədlər siyahısının elementlərinin hasilini tapan bir
funksiya yazın. Siyahı funksiyaya parametr kimi ötürülür.
Funksiyanın qaytardığı nəticə hasil olur.
Tapşırıq 2
Tam ədədlər siyahısının elementlərindən ən kiçiyini tapan bir funksiya yazın.
Siyahı funksiyaya parametr kimi ötürülür. Funksiyanın qaytardığı nəticə
siyahının ən kiçik ədədi olur.
Tapşırıq 3
Tam ədədlər siyahısının sadə elementlərinin sayını tapan bir funksiya yazın.
Siyahı funksiyaya parametr kimi ötürülür. Funksiyanın qaytardığı nəticə
siyahının sadə elementlərinin sayı olur.
Tapşırıq 4
Tam ədədlər siyahısından müəyyən elementi silən bir funksiya yazın.
Funksiyanın qaytardığı nəticə siyahıdan silinmiş elementlərin sayı olur.
Tapşırıq 5
İki siyahını parametr kimi qəbul edən və hər iki siyahının
elementlərindən ibarət bir siyahı qaytaran bir funksiya yazın.
Tapşırıq 6
Tam ədədlər siyahısının elementlərini qüvvətə yüksəldən bir funksiya yazın.
Qüvvətin qiyməti funksiyaya parametr kimi ötürülür. Siyahı da funksiyaya
parametr kimi ötürülür. Funksiyanın qaytardığı nəticə elementləri əvvəlki
siyahının qüvvətə yüksəldilmiş elementləri olan siyahı olur.
'''

# Tapsiriq 1.
'''
num = [1, 5, 10, 15]
multi = 1
for i in num:
 multi *= i
print(f'Ededlerin hasili {multi}-dir')

def func(num):
    multi = 1
    for i in num:
        multi *= i
    return multi
'''
# Tapsiriq 2.
'''
def minum(number):
    min = number[0]
    for i in number:
        if i < min:
            min = i
    return min

number = [12, 5, 9, 16, 48]
print(f'Listdeki en kicik eded {minum(number)}-dir')

'''

# Tapsiriq 3.
'''
def sade(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(sade(11))
'''

# Tapsiriq 4.
'''
def remove(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
list = [12, 3, 4, 19, 16]
print(remove(list))
'''

# Tapsiriq 5.
'''
def num(list_1, list_2):
    return list_1, list_2
list_1 = [12, 5, 15, 20, 6]
list_2 = [2, 43, 56, 7]

all_list = list(map(num, list_1, list_2))
print(all_list)
'''
'''
def num(list_1, list_2):
    all_list = []
    for i in num(list_1, list_2):
        all_list.append(i)
    return all_list
print(all_list)
list_1 = [12, 5, 15, 20, 6]
list_2 = [2, 43, 56, 7]
'''
# Tapsiriq 6.
'''
list1 = [7, 5, 10, 15]

listNew = list(map(lambda x: x**2, list1))
print(listNew)
'''