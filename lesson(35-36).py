def mymin(ls):
   minimum = ls[0]
   for i in ls:
      if i < minimum:
         minimum = i
   return minimum
ls = [1,2,10,5,-2,10,100]
print(mymin(ls))


num = 30
def func():
   num = 10 # func
   print(f"Nonlocal: {num}") # func
   def func2():
      nonlocal num
      num = -10 #func
      print(num) #func
   func2()
   print(f"Nonlocal: {num}") # func
print(f"Global num: {num}")
func()
print(f"Global num: {num}")


def tebrik(is_yeri, vezife, depart, ad, tebrik):
   print(f"{is_yeri} {vezife} {depart} {ad} {tebrik}")
def func1(is_yeri):
   def func2(vezife):
      def func3(depart):
         def func4(ad):
            def func5(tebrik):
               print(f"{is_yeri} {vezife} {depart} {ad} {tebrik}")
            return func5
         return func4
      return func3
   return func2
google_tebrikler = func1("Google")("Director")("Programming")
google_tebrikler("John")("Happy Birthday")
google_tebrikler("James")("Tebrik!")
# tebrik("Google", "Director", "Programming", "John", "Happy birthday")
# tebrik("Google", "Programmer", "Programming", "James", "Tebrik edirem")


from datetime import datetime
def linear_search(list, num):
   for i in range(0, len(list)):
      if list[i] == num:
         return i
   return -1
def binary_search(list, num):
   start = 0
   end = len(list)-1
   while start<=end:
      mid = (start+end)//2
      if list[mid]==num:
         return mid
      elif num<list[mid]:
         end = mid-1
      else:
         start = mid+1
   return -1

list = []
for i in range(100000001):
   list.append(i)
# 0-100000
start = datetime.now() # 21:07
binary_search(list, 100000000)
runtime = datetime.now()-start #  21:10-21:07 = 3 deq
print(f"time: {runtime}")


mytuple = (1,2,4,5,6,7,8) # append, pop, remove
mylist = list(mytuple)
mylist.append(9)
mytuple = tuple(mylist)
print(mytuple)





fruit = ('apple, banana, pear, apple')
count_fruit = input('Sayi tapilacaq elementi daxil edin:')
count = 0
for i in fruit:
    if i == count_fruit:
        count += 1
print(count)


marka = input('Marka adi daxil edin:')
m_tuple = ('Range rover', 'Toyota', 'Mercedes', 'Opel')
list = [marka if i == 'Opel' else i for i in m_tuple]
list_2 = tuple(list)
print(list_2)
































