# Tapsiriq 1.

str1 = str(input(' Setir daxil edin: '))
if str1 == str1[::-1]:
    print(f'{str1} polindromdur')
else:
    print(f'{str1} polindrom deyil')

# Tapsiriq 2.

text = input('Bir metn daxil edin: ')   # This is a sample text. sample text. sample text.
reserve_word = input('Rezer sözünü daxil edin: ')
if text.find(reserve_word) == -1:
       print('Not found.')
else:
       text = text.replace(reserve_word, reserve_word.upper())
       print(text)


# Tapsiriq 3.

print(str_comp.count('.'))