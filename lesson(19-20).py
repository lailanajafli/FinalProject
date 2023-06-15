# Sual - cavab
'''

 1. Setir nedir?
 2. İndex nedir?
 3. İndexleme hansı ededden başlayır?
 4. Niye başlanğıc eded 0-dır?
 5. Setrin her hansı elementine nece müraciet olunur? - İndex ile
'''
text = 'Hello World'
print(text[6])
print(text[12])  # IndexError -> out of range
'''
 6. İndex-lerde menfi ededlerden istifade etmek olar mı? Bu zaman ne baş verir?
 7. Setrin uzunluğunu nece tapmaq olar? len() funksiyası ile
 8. İstenilen setrin axırıncı elementine nece müraciet etmek olar?
'''
text = 'Hello World'
print(text[6])
print(text[-1])
print(text[len(text)-1])
'''
 9. String Slicing nedir? Setrin indexlere göre parçalanması
'''
text = 'Hello World'
print(text[9:])
print(text[:11])
'''
10. String Slicing-de addım?
'''
text = 'Hello World'
print(text[::3])
print(text[9:3:-3])
'''
11. Setirler ile iş. Hansı emeller aparıla biler?
'''
text = 'Hello '
text2 = 'World'
print(text + text2)
text3 = text * 4
print(text3)
'''
12. Built-in metodlar nedir?
13. Funksiya nedir? 
14. Metod nedir?
'''
# objectName.methodName()
'''
15. Setir metodları (built-in metodlar)? Setrin metodları orijinal setri deyişir mi?
16. Setirlerde formatlama (formatting)?
'''
text = 'Hello World!'
print(text.center(50, '#'))
print(text.ljust(50, '#'))
print(text.rjust(50, '#'))

text = '      Hello World!    '
print(text.strip())

text = r'Hello \n\t World!'  # raw string
print(text)

message = 'Hello'
text = f'Your message is {message}'
print(text)

# .format() metodu
message = 'Hello'
text = 'Your message is {}'.format(message)
print(text)
'''

17. Setirlerde axtarış?
'''
text = 'Hello World!'
# text.find('H'), text.rfind('W')
# text.index('H'), text.rindex('W')
# IN ve NOT IN
if 'H' in text:
  print('Mövcuddur')
if 'as' not in text:
  print('Mövcud deyil')
'''
18. Setirlerde evezetme?
'''
text = 'Hello ello ello'
print(text.replace('el', 'lleo', 2))
'''
19. .replace() metodunun arxasında hansı kod işleyir?
'''
# 1 herf üçün      arxada isleyen kod
text = 'This is a sample text'  # bütün a herfleri * ile evez olunsun
new_text = ''
for i in text:
  if i == 'a':
    i = '*'
  new_text += i
print(new_text)
'''
20. Setirlerde check metodları? 
21. .split() metodu
'''
text = 'This is a sample text. Sample text. Sample text.'
print(text)
print(text.split())
print(text.split('. '))
'''
22. .join() metodu
'''
text = 'hello'
joined_text = '*'.join(text)
print(joined_text)

text = 'This is a sample text. Sample text. Sample text.'
print(text)
sentence = text.split('. ')
print('&&'.join(sentence))
'''
23. Kitabxana nedir?
24. Random kitabxanası ne üçündür? Keçdiyimiz metodlar?
'''
import random
print(random.random())
print(random.randint(-90, 100))
print(random.uniform(-90, 100))
print(random.choice('Hello'))
'''
25. .sample() metodu -> geri qaytarılan deyer list-dir, siyahıdır.
'''
import random
new_var = random.sample('HelloWorld!', 10)
print(new_var)
print(''.join(new_var))
'''
26. ASCII nedir?
27. ASCII-de bir simvolun teqdim olunması üçün neçe bit-den istifade olunur?
28. ASCII elifbasının gücü?
29. String kitabxanası, metodlar?
'''
import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
print(string.printable)
'''
30. chr() ve ord() funksiyaları?
    .ascii_lowercase metodunun arxasında hansı kod işleyir?
'''
for i in range(97, 123):
  print(chr(i), end='')


# Ev Tapşırığı
# Tapşırıq 1.
# İstifadəçi klaviaturadan bir arifmetik ifadə daxil edir. Məsələn, 23+12.
# İfadənin hesablanması nəticəsini ekranda göstərmək lazımdır. Bu nümunədə bu, 35-dir.
# İfadə yalnız üç hissədən ibarət ola bilər: ədəd, əməl, ədəd. Mümkün əməllər: +, -,*,/.

expression = input('Ededi ifade daxil edin. Meselen (12+23): ')
if '+' in expression:
  num1, num2 = expression.split('+')  # [12, 23]
  sum = int(num1) + int(num2)
  print(f'{num1} + {num2} = {sum}')
elif '-' in expression:
  num1, num2 = expression.split('-')  # [12, 23]
  difference = int(num1) - int(num2)
  print(f'{num1} - {num2} = {difference}')
elif '*' in expression:
  num1, num2 = expression.split('*')  # [12, 23]
  multiplication = int(num1) * int(num2)
  print(f'{num1} * {num2} = {multiplication}')
elif '/' in expression:
  num1, num2 = expression.split('/')  # [12, 23]
  division = int(num1) / int(num2)
  print(f'{num1} / {num2} = {division}')
else:
  print('!!!Düzgün ifade daxil edin!!!')




#Tekrar. Yuxarıdakı meseleni ele deyişdirin ki istifadeçi sonsuz sayda hesablama apara bilsin.
try:
  while True:
    expression = input('Ededi ifade daxil edin. Meselen (12+23): ')
    if '+' in expression:
      num1, num2 = expression.split('+')  # [12, 23]
      sum = int(num1) + int(num2)
      print(f'{num1} + {num2} = {sum}')
    elif '-' in expression:
      num1, num2 = expression.split('-')  # [12, 23]
      difference = int(num1) - int(num2)
      print(f'{num1} - {num2} = {difference}')
    elif '*' in expression:
      num1, num2 = expression.split('*')  # [12, 23]
      multiplication = int(num1) * int(num2)
      print(f'{num1} * {num2} = {multiplication}')
    elif '/' in expression:
      num1, num2 = expression.split('/')  # [12, 23]
      division = int(num1) / int(num2)
      print(f'{num1} / {num2} = {division}')
    else:
      print('!!!Düzgün ifade daxil edin!!!')
      break
except ValueError:
  print('Yanlış ifade!!!')

# Tapşırıq 2.
# Təsadüfi tam ədədlər sətrində ən kiçik və ən böyük elementləri müəyyənləşdirin,
# mənfi elementlərin sayını tapın, müsbət elementlərin sayını tapın, sıfırların sayını tapın.
# Nəticələri ekranda əks etdirin.
import random

max = 0
min = 0
neg_count = 0
pos_count = 0
zero_count = 0
count = 0    # ümumi count -> random daxiletmelerin sayı
string_of_integers = ''

for i in range(20):
  random_number = random.randint(-80, 101)   # 12, 14, 9, -5
  string_of_integers += str(random_number) + ' '
  count += 1
  if count == 1:
    max = random_number  # max = 12
    min = random_number  # min = 12
  if random_number > max:
    max = random_number  # max = 14
  if random_number < min:
    min = random_number

  if random_number > 0:
    pos_count += 1
  elif random_number < 0:
    neg_count += 1
  else:
    zero_count += 1

print(string_of_integers)
print(f'Minimum is {min}')
print(f'Maximum is {max}')
print(f'Zero numbers count is {zero_count}')
print(f'Positive numbers count is {pos_count}')
print(f'Negative numbers count is {neg_count}')

# Evvel etdiyimiz tapşırıq.
# İstifadəçi klaviaturadan bir neçə ədəd daxil edir.
# Proqram daxil edilmiş ədədlərin cəmini, onlardan ən böyüyünü və ən kiçiyini tapmalıdır.
# İstifadəçi klaviaturadan 7 ədədini daxil etdikdə, proqram işini dayandırır və
# ekranda “Good bye!” yazısı əks olunur.

sum = 0
min = 0
max = 0
count = 0
while True:
  number = float(input('Eded daxil edin: '))
  count += 1
  if count == 1:
      min = number
      max = number
  sum += number
  if number == 7:
    print('Good Bye!')
    break
  if number >= max:
    max = number
  if number < min:
    min = number

print(f'{max} is maximum number')
print(f'{min} is minimum number')
print(f'{sum - 7} is total sum')


# Meseleler.
# Tapşırıq 1. Verilmiş metndeki bütün a herflerini silen proqram yazın. Her 2 üsul ile.




# Tapşırıq 2.
# Müəyyən mətn var. Aşağıdakı funksionallığı həyata keçirin:
#   Mətni elə dəyişdirin ki, hər bir cümlə böyük hərf ilə başlasın;
#   Rəqəmlərin mətndə neçə dəfə rast gəldiyini hesablayın;
#   Mətndə durğu işarələrinin neçə dəfə rast gəldiyini hesablayın;
#   Mətndəki nida işarələrinin sayını hesablayın.

text = "this is a sample text. it contains multiple sentences. " \
       "You should count them. also, how many punctuation marks are there. " \
       "let's find out!!!"

sentences = text.split('. ')
new_text = ''
for element in sentences:
  capitalized_element = element.capitalize()
  new_text = new_text + capitalized_element + '. '
print(new_text)

# Metndeki reqemlerin sayının tapılması
digit_count = 0
for i in text:
  if i.isdigit():
    digit_count += 1

# Metndeki durğu işarelerinin sayı
punctuation_count = 0
for i in text:
  if i in '.,':
    punctuation_count += 1

# Metndeki nida işarelerinin sayı
nida_count = text.count('!')




