# Funksiyalar
# Funksiya nedir? -> müeyyen bir işi yerine yetiren ve tekrar-tekrar istifade oluna bilen
# kod bloklarıdır. Funksiyalar ümumi proqram kodunu daha kiçik hisselere ayırmaqla, modullara bölme
# imkanı verir, bu ise proqramın oxunarlığını daha asan edir.

# Function declaration -> funksiya elanı.
# Sintaksis: def açar sözü
'''
def function_name():
    function_body
'''
# Example

def say_hi():
    print('Hi, World!')

# Funksiyanın çağrılması:
say_hi()
say_hi()
say_hi()

print(say_hi) # -> bele yazı bize funksiyanın ünvanını (address) çapa verir
address_variable = say_hi  # -> funksiyanın ünvanını address_variable deyişenine menimsedirem
address_variable()

print(say_hi())



# Elbette ki, funksiyanı elan etmeden evvel onu çağırmaq olmaz!

say_hello()    # -> Xeta!

def say_hello():
    print('Hello, World!')

# Adeten, funksiyaların hamısı proqramın evvelinde yazılır.


def say_hello():
    """
    Bu funksiya salamlama işini görür
    """
    print('Hello, World!')

def say_hello():
    """
    Bu funksiya salamlama işini görür
    """
    print('Hello, World!')
    print('Hello, World!')
    print('Hello, World!')

say_hello()

# Funksiya yaratmağın qaydaları var.
# Ideal funksiyalar nece olur:
# 1) Funksiyanın adı onun gördüyü işe uyğun olmalıdır, ve her bir funksiya tek bir işi yerine yetirmelidir.
# Yeni, 1 funksiya = 1 iş. Meselen, telebenin elave edilmesi -> add_student()

# 2) Funksiyanın ne iş gördüyü barede comment-i olmalıdır.
# 3) Funksiya adının kiçik herfden başlaması tövsiyye olunur.
# 4) Eyni adda tek bir funksiya olmalıdır. Bir neçe eyni adda funksiya olarsa,
# bunlardan en axırıncısı icra olunar.



# Funksiya istifade etmeyin üstünlükleri:
# 1) ümumi proqram kodu modullara ayrılmaqla strukturlaşır, işimiz asanlaşır
# 2) kod yığcam olur
# 3) kod tekrarının qarşısı alınır. Meselen, find_student().
# DRY prinsipi -> Don't Repeat Yourself -> Özünü tekrarlama




# Tapşırıq:
# Aşağıda qeyd olunmuş metni olduğu kimi ekrana çap eden funksiya yazın.
'''
    “Don't let the noise of others' opinions
    drown out your own inner voice.”
                                Steve Jobs
'''

def print_string():
    print('''
    “Don't let the noise of others' opinions
    drown out your own inner voice.”
                                Steve Jobs
''')

print_string()

def print_string():
    print('\t\t“Don\'t let the noise of others\' opinions \n\t\tdrown out your own inner voice.” \n\t\tSteve Jobs')

print_string()



# Funksiyanın parametrleri
sum(arguments) # -> ötürdüyümüz deyerler arqument adlanır,
# funksiya üçün ise bunlar parameter adlanır.

# Funksiyanın parametrleri, sintaksis:

def function_name(param1, param2, ..., paramN):
    # function_body


# Example 1: 2 ededin qiymetini toplamaq funksiyası.
def sum_(number1, number2):
    print(number1 + number2)

a = 16
b = 35
sum_(a, b)


# Example 2:
def sum_(a, b):
    a = 41   # -> bunlara deyirler lokal deyişenler
    b = 52
    print(a + b)

a = 16   # -> bu deyişenlere deyirler qlobal deyişenler
b = 35
# funksiya çağrılmazdan evvel
print(a, ' ', b)
sum_(a, b)
# funksiya çağrılmazdan sonra
print(a, ' ', b)

# Visibility scope -> görünürlük sahesi
# global açar sözü -> funksiya daxilinde funksiyanın xaricinde olan deyişeni
# çağırmaq üçündür
def sum_():
    global a
    global b
    a = 41   # -> bunlara deyirler lokal deyişenler
    b = 52
    print(a + b)

a = 16   # -> bu deyişenlere deyirler qlobal deyişenler
b = 35
# funksiya çağrılmazdan evvel
print(a, ' ', b)
sum_()
# funksiya çağrılmazdan sonra
print(a, ' ', b)


# Tapşırıqlar

# Tapşırıq 1
# Parametr kimi iki ədəd qebul eden və bu ededler
# arasındakı bütün tək ədədləri çap eden funksiya yazın.

def odd_numbers(start, end):
    for i in range(start, end + 1):
        if i % 2 == 1:
            print(i, end=' ')


start_num = int(input('Başlanğıc ededini daxil edin: '))
end_num = int(input('Son ededi daxil edin: '))
odd_numbers(start_num, end_num)



# Tapşırıq 2
# Müeyyen simvoldan ibaret üfüqi və ya şaquli xətt çap eden funksiya yazın.
# Funksiya parametr kimi qəbul edir: xəttin uzunluğu, istiqamət, simvol.

def line_of_symbols(length, direction, symbol):
    for i in range(length):
        if direction == 'horizontal':
            print(symbol, end=' ')
        if direction == 'vertical':
            print(symbol)



line_of_symbols(15, 'horizontal', '+')

# Qeyd 1: Arqumentler parametrlere ardıcıl olaraq menimsedilir.
# Buna göre de arqumentlerin deyeri adeten bire bir deqiq ardıcıllıqla teyin olunur.

# Amma, bu ardıcıllığı aşağıdakı şekilde de yazmaq olar
def line_of_symbols(length, direction, symbol):
    for i in range(length):
        if direction == 'horizontal':
            print(symbol, end=' ')
        if direction == 'vertical':
            print(symbol)


line_of_symbols(direction='horizontal', length=11, symbol='%')



# Qeyd 2. Parametrlerin susmaya göre (default) deyerleri ola biler.
def line_of_symbols(length, direction, symbol = '!'):
    for i in range(length):
        if direction == 'horizontal':
            print(symbol, end=' ')
        if direction == 'vertical':
            print(symbol)


line_of_symbols(11, 'horizontal', '{')


# Funksiyalar 2 cür olur:
# 1) müeyyen işi icra eden: .remove()
# 2) müeyyen işi icra etdikden sonra deyer qaytaran: .pop()

example_list = [123, 456]
print(example_list.remove(123))
print(example_list.pop(0))

# !!! Qeyd: çapa vermek -> deyer qaytarmaq demek deyil!!!

# Funksiyada deyerin qaytarılması return operatoru ile heyata keçirilir.
# Example

def say_hi():
    string = 'Hello, World!'
    return string

say_hi()
print(say_hi())


def say_hi():
    return True


print(say_hi())

# Funksiyada deyerin qaytarılması return operatoru ile heyata keçirilir.
# Example
# Qeyd: return setrinde hansı tipde deyer qeyd olunubsa, o tipde deyer
# funksiyanın çağrıldığı yere qayıdır.
# Example:

def say_hello(name):
    return f'Hello, {name}'


print(say_hello('Emin').upper())
print(say_hello('Leyla'))
print(say_hello('Mirteyyub').upper())


# Qeyd 2: return operatoru her bir funksiya üçün 1 defe icra oluna biler.
# Funksiya daxilinde return operatoru icra olunduqda, bize müvafiq deyer qayıdır,
# proqramın işi dayanır, ve artıq return sözünden sonrakı kodlar var olsalar bele
# heç biri oxunmur, yeni, icra olunmur.

# Example

def is_odd_number(number):
    if number % 2 == 1:
        return True
    if number % 2 == 0:
        return False
    print('Hello Hello Hello')
    return 'hello hello'


print(is_odd_number(10))



# Tapşırıqlar.

# Tapşırıq 1.
# Faktorialın hesablanması funksiyasını yazın:
# Giriş kimi n tam ədədini qəbul edən və n-in faktorialını qaytaran find_factorial adlı funksiya yazın.
# Məsələn, 5-in faktorialı (5 kimi qeyd olunur!) 5 * 4 * 3 * 2 * 1 = 120-dir.

def find_factorial(param_num):
    if param_num <= 0:
        return False
    factorial = 1
    while param_num > 0:
        factorial *= param_num
        param_num -= 1
    return factorial

input_number = int(input('Eded daxil edin: '))
print(find_factorial(input_number))

# Tapşırıq 2.
# Ededin sade olub olmadığını yoxlayan funksiya yazın:
# Parameter kimi tam ədədi qəbul edən və eded sadə ədəddirsə True, əks halda isə False qaytaran
# is_prime adlı funksiyanı həyata keçirin.
# Sadə ədəd 1 və özündən başqa müsbət bölənləri olmayan 1-dən böyük natural ədəddir.

def is_prime(param_num):
    if param_num <= 1:
        return False
    count = 0
    for i in range(1, param_num + 1):
        if param_num % i == 0:
            count += 1
    if count == 2:
        return f'{param_num} sade ededdir'
    else:
        return f'{param_num} sade eded deyil'


input_number = int(input('Eded daxil edin: '))
print(is_prime(input_number))



# Tapşırıq 3.
# Verilmiş uzunluqda random ededler ile siyahının
# doldurulması funksiyasını yazın.
# Funksiya parameter olaraq uzunluq qebul edir.






