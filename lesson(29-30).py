import datetime
import time
# datetime kitabxanasının metodları:
print(datetime.datetime.today())  # -> cari tarixi ve zamanı qaytarar

print(datetime.date.today())  # -> sadece cari tarixi qaytarar
print(datetime.date.today().year)
print(datetime.date.today().month)
print(datetime.date.today().day)


# time kitabxanasının metodları: .sleep(), .time(), .ctime()
time.sleep(2)  # -> proqrama 2 saniye gözle deyir
time_in_seconds = time.time()    # -> 1970-ci il yanvarın 1-den başlayaraq cari zamana qeder
print(time_in_seconds)           # keçen saniye sayını qaytarır

print(time.ctime(time_in_seconds))  # -> verilmiş saniyelere müvafiq tarixi qaytarar
'''


# Ev tapşırığı:
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
        [11] --> email daxil edilmiş telebenin melumatlarının yenilenmesi
        [0]  --> EXIT
'''

print(menu)

index_name, index_surname, index_father, index_email, index_birth, index_group, index_grade = 0, 1, 2, 3, 4, 5, 6

#               0         1         2              3           4            5                 6
student_1 = ['Leyla', 'Necefli', 'Muxtar', 'leyla@gmail.com', 2000, 'ONLINE_22_PYTHON', [12, 9, 6]]
student_2 = ['Emin', 'Manaflı', 'Elnur', 'emin@gmail.com', 2006, 'ONLINE_22_PYTHON', [12, 12]]

all_students = [student_1, student_2]


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
        input_email = input('Telebenin email ünvanını daxil edin: ')
        check = False

        for student in all_students:
            if student[index_email] == input_email:
                check = True
                print('Verilmiş telebenin qiymetler siyahısı: ', end='')
                for grade in student[index_grade]:
                    print(grade, end=', ')

        if not check:
            print('Bu email ünvanında telebe mövcud deyil')

    elif user_input == '6':
        print()
        input_email = input('Telebenin email ünvanını daxil edin: ')
        check = False

        for student in all_students:
            if student[index_email] == input_email:
                check = True
                print(f'{student[index_name]} {student[index_surname]} {student[index_father]} yaşı: ', end=' ')
                print(f'{datetime.date.today().year - student[index_birth]}')

        if not check:
            print('Bu email ünvanında telebe mövcud deyil')

    elif user_input == '7':
        print()
        input_group = input('Axtarılan qrup adını daxil edin: ').upper()
        count = 1
        for student in all_students:
            if student[index_group] == input_group:
                print(f'{count}) {student[index_name]} {student[index_surname]} \
{student[index_father]} {student[index_email]} {student[index_group]}')
                count += 1
        if count == 1:
            print('Bu adda qrup mövcud deyil')

    elif user_input == '8':
        print()
        count = 1
        for student in all_students:
            print(f'{count}) {student[index_name]} {student[index_surname]} {student[index_father]} \
{student[index_email]} {student[index_group]} {student[index_grade]} ')
            count += 1
    elif user_input == '9':
        print()
        print(menu)
        print()

    elif user_input == '10':
        print()
        input_email = input('Telebenin email ünvanını daxil edin: ')
        check = False
        grade_sum = 0
        count = 0

        for student in all_students:
            if student[index_email] == input_email:
                check = True
                grade_sum = sum(student[index_grade])
                count = len(student[index_grade])
                if count == 0:
                    print('Telebenin helelik qiymeti yoxdur')
                else:
                    print(f'Qiymet ortalaması: {grade_sum / count}')

        if not check:
            print('Bu email ünvanında telebe mövcud deyil')


    # email ünvanı daxil olunmuş telebenin yenilenmesi
    elif user_input == '11':
        print()
        input_email = input('Yenilemek istediyiniz telebenin email ünvanını daxil edin: ')
        check = False

        for student in all_students:
            if student[index_email] == input_email:
                check = True

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
                    if input_email.endswith('gmail.com') or input_email.endswith('mail.ru') and input_email.count(
                            '@') == 1 and len(input_email) >= 12:

                        check = True
                        index_number = -1
                        for student in all_students:
                            index_number += 1
                            if student[index_email] == input_email and all_students[index_number] != student:
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

                # Update
                student[index_name] = input_name
                student[index_surname] = input_surname
                student[index_father] = input_father
                student[index_email] = input_email
                student[index_birth] = input_birth
                student[index_group] = input_group

                print('Telebe melumatları uğurla yenilenmişdir!')
                time.sleep(1)
                break

        if not check:
            print('Bu email ünvanında telebe mövcud deyil')


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




# Sorting algorithms -> çeşidleme alqoritmleri
# Çeşidleme -> verilmiş elementleri müeyyen qaydada sıralamaqdır, düzmekdir

# Artan qaydada -> kiçik elementden böyük elemente doğru
# Azalan qaydada -> böyük elementden kiçik elemente doğru

# sorting methods: .sort()

example_list = [5, 7, 3, 8, 1, 2]

# Artan qaydada
example_list.sort()
print(example_list)


# Azalan qaydada
example_list.sort(reverse=True)
print(example_list)


# Siyahını tersine çeviren metod: .reverse() metodu
example_list = [5, 7, 3, 8, 1, 2]
example_list.reverse()
print(example_list)



# Python .sort() metodunun arxa fonunda Timsort adlanan alqoritmden istifade edir:
# Timsort alqoritmi Insertion sort ve Merge sort alqoritmlerin hybryd-idir


# Sorting alqorithmlerinin növleri:
# 1) Bubble Sort
# 2) Insertion Sort
# 3) Merge Sort
# 4) Quick Sort

 


# Bubble sort  -> artan qaydada
example_list = [7, 5, 3, 8, 1, 2]
for run in range(len(example_list) - 1):
    for i in range(len(example_list) - 1):
        if example_list[i] > example_list[i+1]:
            # swap xüsusiyyeti
            example_list[i], example_list[i+1] = example_list[i+1], example_list[i]

print(example_list)


# Bubble sort  -> azalan qaydada
example_list = [7, 5, 3, 8, 1, 2]
for run in range(len(example_list) - 1):
    for i in range(len(example_list) - 1):
        if example_list[i] < example_list[i+1]:
            # swap xüsusiyyeti
            example_list[i], example_list[i+1] = example_list[i+1], example_list[i]

print(example_list)





# Insertion Sort alqoritmi -> Daxiletme ile çeşidleme

example_list = [7, 5, 3, 8, 1, 2]
length = len(example_list)

for i in range(1, length):
    key = example_list[i]
    j = i - 1

    while example_list[j] > key and j >= 0:
        example_list[j+1] = example_list[j]
        j = j - 1
        print(example_list)

    example_list[j + 1] = key
    print(example_list)
print(example_list)





