'''


# Rekursiya nedir? Funsiya ozunu oz icersinde cagirir
# Lambda funksiyasi yanliz 1 setirde yazila biler,
# funksiyaya ad vermeye ehtiyac qalmir ve aca sozunden istifade etmek olur,
# 1 defe cagira bilerik

def hasil(start, end):
    if start>end:
        print("Error")
        return
    else:
        num = 1

def hasil(start, end):
    if start>end:
        print("Error")
        return
    else:
        num = 1
        for i in range(start, end+1): # 5, 10 -> 5,6,7,8,9
            num *= i
        print(num)
        return num

def func(func1, start, end, mult):
    return func1(start, end)*mult

result = func(hasil, 5, 7, 2)
print(result)


def palind(myStr):
 if len(myStr) == 0:
   return True
 else:
   if myStr[0] == myStr[-1]:
     return palind(myStr[1:-1])
   else:
     return False

print(palind("madam"))

# madam ->  madam
# level -> level


students = [['Bob22', 70], ['Jane111', 80], ['Bod', 50]]
print(students)
sortedSts = sorted(students, key=lambda x: x[1])
print(sortedSts)


def func(num):
 return num*2
list1 = [1, 5, 10, 15]

#-------
listNew = list(map(func, list1))
print(listNew)
#------
listNew2 = []
for i in list1:
 listNew2.append(func(i))
print(listNew2)
'''
import random

'''
list = [5, 10, 15, 100]
newlist = []

for i in list:
    if i < 100:
        newlist.append(i)
print(newlist)
'''

'''
list1 = ['Bob', 'John', 'James']
new_list = list(filter(lambda x: x[1] == 'o', list1))
print(new_list)
'''

def func(mylist, num):
 counter = 0
 for i in mylist:
  if i==num:
   counter += 1
 return counter
def sum(list):
 mysum=0
 for i in list:
  mysum+=i
 return mysum
def average(list):
 return sum(list)/len(list)

mylist = []
for i in range(3):
 mylist.append(int(input("Enter a number: ")))
num = int(input("Enter number to find: "))
print(func(mylist, num))
print(sum(mylist))
print(average(mylist))




























