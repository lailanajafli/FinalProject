# Tapsiriq 1-ci

#1. print(string.ascii_lowercase)
# Arxada isleyen kod

for i in range(97, 123):
  print(chr(i), end='')
print()

#2. print(string.ascii_uppercase)
# Arxada isleyen kod

for i in range(0, 25):
    print(chr(i+65), end='')


#3. print(string.ascii_letters)
# Arxada isleyen kod

for i in range(0, 25):
    print(chr(i+65), end='')
for i in range(97, 123):
  print(chr(i), end='')


#4. print(string.digits)
# Arxada isleyen kod
for i in range(48, 58):
  print(chr(i), end='')
print()


#5. print(string.punctuation)
# Arxada isleyen kod

for i in range(20, 48):
  print(chr(i), end='')
print()


#6. print(string.printable)
# Arxada isleyen kod

for i in range(0, 128):
  print(chr(i), end='')
print()




# Tapşırıq 2.
# İstifadeçi yaradılacaq olan şifrede neçe böyük herf neçe kiçik herf,
# neçe reqem, neçe işare olduğunu daxil edir.
# buna esasen şifre yaradılır ve ekrana çap olunur.

import random
import string

uppercase = int(input("Şifredeki böyük herf sayını daxil edin: "))
lowercase = int(input("Şifredeki kicik herf sayını daxil edin: "))
digits = int(input("Şifredeki reqem sayını daxil edin: "))
symbols = int(input("Şifredeki simvol sayını daxil edin: "))

password = ''
password += ''.join(random.sample(string.ascii_lowercase, lowercase))
password += ''.join(random.sample(string.ascii_uppercase, uppercase))            bu da basqa formasi
password += ''.join(random.sample(string.digits, digits))
password += ''.join(random.sample(string.punctuation, symbols))

# Yaradılmış şifreni qarışdırmaq üçün
print(password)

password_randomize = random.sample(password, len(password))
password = ''.join(password_randomize)

print(password)
'''

import random
import string
password = 0
password_upper = random.sample(string.ascii_uppercase, 6)                       bu men yazan duzdu
password_islower = random.sample(string.ascii_lowercase, 5)
password_digit = random.sample(string.digits, 4)
password_punctuation = random.sample(string.punctuation, 3)
printable = password_upper + password_digit + password_punctuation + password_islower
printable = ''.join(printable)
print(printable)








