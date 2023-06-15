'''
       #01234
text = 'Hello'
print(len(text))

text = 'skdjahkdsjah asdjahskdahskd dfkahdgkasjhdka!'
# sonuncu index her zaman beraberdir: len(text) - 1
print(text[len(text)-1])

print(text[2:9])
print(text[:])
print(text[:: 2])
'''
'''
multi_line = '''
              #^^^^^^^^^
         #welcome to Academy.
         #^^^^^^^^^^^^^^^^^^^
'''
print(multi_line)
'''
'''
import random

print(random.random()) # -> 0 ile 1 arasında olan tesadüfi deyer
print(random.randint(-90, 100)) # -> verilmiş diapazonda tesadüfi integer deyer
print(random.uniform(-90, 100)) # -> verilmiş diapazonda tesadüfi kesr deyer
print(random.choice('string deyer olmalıdır')) # -> verilmiş setirde tesadüfi element
'''


# Tapşırıq 1.
# İstifadəçi klaviaturadan sətir daxil edir.
# Sətirdəki hərflərin, rəqəmlərin ve boşluqların sayını hesablayın
# ve setrin ümumi uzunluğunu hesablayın.
# Hər bir ədədi ekranda çap edin.
'''
user_input = input('Setir daxil edin: ')
count_alpha = 0
count_digit = 0
count_space = 0
for element in user_input:
       if element.isalpha():
              count_alpha += 1
       elif element.isdigit():
              count_digit += 1
       else:
              count_space += 1

print(count_alpha)
print(count_digit)
print(count_space)
print(len(user_input))
'''

# Sual - cavab. Nested if-ler?

# Tapşırıq 2.
# İstifadeçi şifre daxil edir. Şifrenin güclü olub olmadığını yoxlamaq lazımdır.
# Güclü şifre terkibinde en azı 8 simvol olmalıdır, en azı 1 böyük herf,
# en azı 1 kiçik herf, en azı 1 reqem, en azı 1 işare olmalıdır.
# İstifade olunmalıdır: string check metodları, iç içe if-ler
'''
password = input('Şifre daxil edin: ')
if len(password) >= 8:
       if password.isupper() or password.islower():
              print('Minimum 1 böyük herf, minimum 1 kiçik herf olmalıdır')
       else:
              if password.isdigit():
                     print('Minimum 1 herf olmalıdır')
              else:
                     if password.isalnum():
                            print('Minimum 1 işare olmalıdır')
                     else:
                            print('Bu şifre güclüdür')
else:
       print('Şifre en azı 8 elementden ibaret olmalıdır.')
'''

# Yeni metodlar.
# String formatting
'''
text = 'Hello'
print(text.center(20, '#')) # -> ümumi setrin uzunluğunu 20-ye tamamlayır,
                            #    setrimizin mezmununu merkezleşdirir
                            #    tamamlayıcı simvol 2-ci arqumentdeki simvol olur

print(text.ljust(20, '+')) # -> ümumi setrin uzunluğunu 20-ye tamamlayır, setrimiz ise soldan yazılır
print(text.rjust(20, '-')) # -> ümumi setrin uzunluğunu 20-ye tamamlayır, setrimiz ise sağdan yazılır

text = '          Hello        '
print(text)
print(text.strip())
print(text.lstrip()) # -> soldakı boşluqları silecek
print(text.rstrip()) # -> sağdakı boşluqları silecek

# raw stringler
text = r'This is sample \n text.'            # escape sequensisleri yox eliyir
text2 = 'This is the Browns\'s home'
print(text2)
'''
'''
# .format() metodu
user_login = input('Enter your nick name: ')
str_msg = 'Hello, {} user.'.format(user_login)
print(str_msg)+

salary_msg = 'Hello, your salary is {0:3.2f}'.format(200.7873)
print(salary_msg)
'''
# Setirlerde axtarış
# .find() metodu, .rfind() metodu
'''
text = 'Dobby is free'
print(text.find('is', 7, len(text)-1))
print(text.find('by')) # -> soldan sağa axtarış aparır
print(text.rfind('by')) # -> sağdan sola axtarış aparır
'''
'''
# .index ve .rindex metodları
text = 'Dobby is free'
print(text.index('is', 7, len(text)-1))
print(text.index('by')) # -> soldan sağa axtarış aparır
print(text.rindex('by')) # -> sağdan sola axtarış aparır
# index ile find fergi: altsetir tapılmadıqda find -1 qaytarır 
# index ise ValueError qaytarır

# IN ve NOT IN açar sözleri
text = 'Dobby is free'
if 'free' in text:
       print(True)
if 'asd' not in text:
       print(False)
'''
# Setirlerin bölünmesi
# .split() metodu
# setri hisselere parçalayır ve hemin hisseleri bir siyahıya yığır.
# susmaya göre setirler boşluğa göre parçalanır
# arqument ile bunu deyişmek olar
'''
text = 'This is a sample text. sample text. sample text'
print(text.split())
#print(text.split('a'))
#print(text.split('.'))

# Setirlerin birleşdirilmesi
# .join() metodu
# istenilen sayda element birleşdirir
print('+'.join(text.split()))
'''

# Tapşırıq.
# Bir metnimiz var. bu metnde bütün cümleler kiçik herf ile başlayır.
# Metndeki her bir cümle böyük herf ile başlasın.
'''
text = 'this is a sample text. sample text. sample text. text.'
print(text)

sentences = text.split('. ')
print(sentences)
capitalized_sentences = ''

for sentence in sentences:
       sentence = sentence.capitalize()
       capitalized_sentences += sentence + '. '

print(f'{capitalized_sentences[: len(capitalized_sentences)-2]}')
'''

# string modulu
'''
import string

print(string.ascii_uppercase)  # Arxada hansı kod işleyir?
# chr() ve ord() funksiyaları
'''
'''
print(chr(65))
for i in range(0, 25):
       print(chr(i+65), end='')
'''
'''
print(string.ascii_lowercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)
'''
'''
import string
import random

# random kitabxanasının .sample() metodu
# print(random.sample(string.ascii_lowercase, 6))
lowercase = random.sample(string.ascii_lowercase, 6)
print(lowercase)
#.sample() metodunda qaytarılan deyer siyahıdır, yeni, list-dir

#.join() metodunda qaytarılan deyer setirdir.
print(''.join(lowercase))
'''
# Tapşırıq. İstifadeçi uzunluq daxil edir.
# Verilmiş uzunluqda istifadeçi üçün username yaradılmalıdır.
# username ibaretdir: kiçik herfler + reqemler
import string
import random
length = int(input('Username üçün uzunluq daxil edin: ')) #10
username = random.sample(string.ascii_lowercase + string.digits, length)
username = ''.join(username)
print(f'Your username is  {username}.')
