# random.shuffle() -> qarışdırmaq, arqument olaraq list qebul edir, ve hemin listin elementlerini qarışdırır

example_list = [1, 2, 3, 4, 5] # -> 1-ölçülü siyahı

example_list = [[1, 2, 3], [2, 4, 6], [3, 5, 7], [4, 7, 9], [5, 6]]  # 2-ölçülü siyahı
print(example_list[1][1])

for i in range(5):
    example_list.append(i)


example_list_2 = [i for i in range(5)]
print(example_list)
print(example_list_2)

example_list_3 = [input(), input(), input()]


# Nested lists -> İç içe siyahılar


# Ev tapşırığı

# Tapşırıq 1.
'''
İç içe siyahıdakı bütün elementlərin cəmini çap edən kodu yazın.
'''

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




# datetime ve time kitabxanaları ->
# tarix ve zaman ile işlemeye imkan veren modullardır

# datetime kitabxanası tarix (date) ve zaman (time) ile işlemeye imkan verir
# time kitabxanası saniyeler ile verilmiş zaman ile işleyir

# aralarındakı ferq deqiqlik seviyyesindedir
# layihenin evvelinde kitabxanaları import etmek lazımdır:

import datetime
import time

print(datetime.datetime.today()) # -> cari tarix ve zamanı qaytarır
print(datetime.datetime.today().year)
print(datetime.datetime.today().month)
print(datetime.datetime.today().day)
print(datetime.datetime.now()) # -> cari tarix ve zamanı qaytarır


date = datetime.date(2021, 4, 17) # -> verilmiş deyerleri tarix tipine çevirir
print(date)


# time modulu
time.sleep(2)   # -> arqument olaraq saniye qebul edir,
                # verilmiş saniye qeder proqramın icrasını gecikdirir
# .time() metodu 1970-ci il yanvarın 1-den başlayaraq
# bu güne geder keçen zamanı saniyeler ile bize qaytarır
current_time_in_seconds = time.time()
print(time.time())

# .ctime() metodu -> saniyelerde verilmiş deyeri hemin vaxtdakı tarixe çevirir
import time
current_time_in_seconds = time.time()
print(time.ctime(current_time_in_seconds))




# all_students task

import datetime
import time

menu = '''
        [1]  --> yeni telebe elave etmek
        [2]  --> email seçilmiş telebeni silmek
        [3]  --> ada göre telebe axtarışı
        [4]  --> email daxil edilmiş telebeye qiymet verilmesi
        [5]  --> email daxil edilmiş telebenin qiymetleri
        [6]  --> email daxil edilmiş telebenin yaşı
        [7]  --> eyni qrupda olan telebelerin siyahısı
        [8]  --> bütün telebeler
        [9]  --> SHOW MENU
        [10] --> email daxil edilmiş telebenin qiymet ortalaması
        [0]  --> EXIT
'''

print(menu)

index_name, index_surname, index_father, index_email, index_birth, index_group, index_grade = 0, 1, 2, 3, 4, 5, 6

#               0         1         2              3           4            5                 6
student_1 = ['Leyla', 'Necefli', 'Muxtar', 'leyla@gmail.com', 2000, 'ONLINE_22_PYTHON', [12, 12, 12]]

all_students = [student_1]


while True:
    user_input = input('Menyudan seçim daxil edin: ')

    if user_input == '1':
        print()

        # Adın daxil edilmesi
        while True:
            input_name = input('Ad daxil edin: ').capitalize()
            if input_name.isalpha() and len(input_name) >= 3:
                break
            else:
                print('!!!Düzgün ad daxil edin!!!')

        # Soyadın daxil edilmesi
        while True:
            input_surname = input('Soyad daxil edin: ').capitalize()
            if input_name.isalpha() and len(input_name) >= 3:
                break
            else:
                print('!!!Düzgün soyad daxil edin!!!')

        # Ata adının daxil edilmesi
        while True:
            input_father = input('Ata adı daxil edin: ').capitalize()
            if input_name.isalpha() and len(input_name) >= 3:
                break
            else:
                print('!!!Düzgün ata adı daxil edin!!!')

        # Email daxil edilmesi -> email ünvanı unikal olmalıdır
        while True:
            input_email = input('Email ünvanı daxil edin: ')
            if input_email.endswith('gmail.com') or input_email.endswith('mail.ru') and input_email.count('@') == 1 and len(input_email) >= 12:

                check = True

                for student in all_students:
                    if student[index_email] == input_email:
                        print('!!!Bele email ünvanı sistemde mövcuddur!!!')
                        check = False
                        break

                if check:
                    break

            else:
                print('!!!Düzgün email ünvanı daxil edin!!!')

        # Doğum ilinin daxil edilmesi
        while True:
            input_birth = int(input('Doğum ilini daxil edin: '))
            if input_birth >= datetime.date.today().year - 40 and input_birth <= datetime.date.today().year - 15:
                break
            else:
                print(f'!!!Doğum ili {datetime.date.today().year - 40} ile {datetime.date.today().year - 15} arasında ola biler!!!')


        # Qrupun daxil edilmesi
        while True:
            input_group = input('Qrup daxil edin: ').upper()
            if input_group.isprintable() and len(input_group) >= 3:
                break
            else:
                print('!!!Düzgün qrup adı daxil edin!!!')

        # Qeydiyyat
        new_student = [input_name, input_surname, input_father, input_email, input_birth, input_group, []]

        all_students.append(new_student)
        print('Telebe uğurla elave edilmişdir!')
        time.sleep(1)


    elif user_input == '2':
        print()
        input_email = input('Telebenin email ünvanını daxil edin: ')
        check = False
        for student in all_students:
            if student[index_email] == input_email:
                all_students.remove(student)
                check = True
                break
        if check:
            print('Telebe uğurla sistemden silinmişdir!')
        else:
            print('!!!Bu email ünvanı ile telebe mövcud deyil!!!')



    elif user_input == '3':
        print()
        input_name = input('Axtarılan telebenin adını daxil edin: ')
        count = 1
        for student in all_students:
            if student[index_name] == input_name:
                print(f'{count}) {student[index_name]} {student[index_surname]} {student[index_father]} {student[index_email]} {student[index_group]} ')
                count += 1
        if count == 1:
            print('!!!Daxil edilmiş adda telebe mövcud deyil!!!')

    elif user_input == '4':
        print()
        input_email = input('Telebenin email ünvanını daxil edin: ')
        check = True
        for student in all_students:
            if student[index_email] == input_email:
                check = False
                input_grade = input('Qiymet daxil edin (1-12): ')
                if input_grade.isnumeric():
                    input_grade = int(input_grade)
                    if input_grade >= 1 and input_grade <= 12:
                        student[index_grade].append(input_grade)
                    else:
                        print('!!!Qiymet 1 ile 12 arasında ola biler!!!')
                else:
                    print('!!!Qiymet ededi olmalıdır!!!')
        if check:
            print('Bu email ünvanında telebe mövcud deyil')

    elif user_input == '5':
        print()
        pass
    elif user_input == '6':
        print()
        pass
    elif user_input == '7':
        print()
        pass
    elif user_input == '8':
        print()
        count = 1
        for student in all_students:
            print(f'{count}) {student[index_name]} {student[index_surname]} {student[index_father]} {student[index_email]} {student[index_group]} {student[index_grade]} ')
            count += 1
    elif user_input == '9':
        print()
        print(menu)
        print()
    elif user_input == '10':
        print()
        pass
    elif user_input == '0':
        print()
        print('Bye.')
        time.sleep(1)
        print('Bye..')
        time.sleep(1)
        print('Bye...')
        break
    else:
        print('!!!Seçim yanlışdır!!!')


























































