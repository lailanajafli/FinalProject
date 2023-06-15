'''
A = {5, 9, 12, 6}
B = {1, 8, 13}
B.add(2)
print(B)

#set() -->  Pythonda - tekrar olunmayan nizamsiz indexlenmemis
#elementler topusudur.

list = [1,2,3,5]
print(set(list))

set1 = {1,2,3,4}
set2 = {3,4,10,11}
#print(set1.union(set2)) # |    birlesme
#print(set1.intersection(set2)) # &     kesisme
#print(set1.difference(set2)) # -
print(set1&set2)
print(set1|set2)
print(set1-set2)

discard() ve remove() metodlarindan istifade ederek biz setlerden mueyyen
#bir elementi sile bilerik. BU metodlarin arasindaki yegane ferq ondan ibaretdir ki,
# silinecek element movcud olmadiqda discard() metodu hec bir deyisiklik etmir,
# remove() metodu ise bu halda xeta yaradir.

A.remove(2)
A.discard(100)
print(A)

a = {} -> dictionary(coxluq)
a = {0, 1} icinde element varsa bu artiq setdi
a = set() -> setde bos setir yaratmaq ucun
a = () -> bos tuple
a = tuple() bos tuple

prnit(len(swimming|box|karate

# enumerateye aid misal  ->enumerate siralama kimi edir , elementlerin indexsini qaytarir,
sadece gorunus ucun
for index, element in enumerate(B):
print(f'{index} - {element}')

# frozenset - deyisilmeyen set union falan olar ama add remove falan olmaz
A = frozenset({1,2,3,4,5,6})
B = frozenset ({4,5,6,7,8})
print(type(A))
print(set(A&B)

# dictionary
dict1 = {"name":"John", "surname":"Ivanov", "age": 30, "cars": ["Bmw", "Mercedes"]}
dict1["phone"] = "IPhone 14 Pro"                                                         bele append kimi olur
print(dict1)

del dict["age]
print(dict1)

# item , key, value
dict1.clear()
print(dict1)


dict2 = {"home":"Port Baku", "watch":"Rolex"}
dict1.update(dict2)
print(dict1)


A



#get olanda NOne olur ama bele adi olanda keyerror
# value float bluean zat'
# ama referans tuple, list string
'''

countries = {"Azerbaycan":"Baki"}
while True:
   option = input("1) Elave et\n2) Sil\n3) Deyisdir\n4) Tap\n5) Goster\n6) Cix\nSecin: ")
   if option=="1":
      yeni_olke = input("Enter country: ")
      yeni_paytaxt = input("Enter capital: ")
      countries[yeni_paytaxt] = yeni_olke
   elif option=="5":
      break

print(countries)


# Tapsiriq 2.
A = {'Baki', 'Quba', 'Qebele', 'Seki' }
B = {'Agcabedi', 'Agdam', 'Lenkeran'}
print(A.union(B))

# Tapsiriq 3.
A = {'Baki', 'Quba', 'Qebele', 'Seki' }
B = {'Agcabedi', 'Agdam', 'Lenkeran'}
print(A-B)


#1
olke = ('Azerbaijan', 'Rusiya', 'Iran')
append =input('Iran')
olke.add(append)
print(olke)
#2
delete = input('Silmek istediyiniz olkeni daxil edin:')
olke.pop(delete)
print(olke)
#3
symbol = input('simbol daxil edin:')
for i in olke:
    if symbol in i:
        print(i)

