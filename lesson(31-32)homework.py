
#Tapsiriq 1.

def text():
    print('''
    “Don't compare yourself with anyone in this world…
    if you do so, you areinsulting yourself.”
                                                Bill Gates
''')
text()



# Tapsiriq 2.

def odd_numbers(start, end):
    for i in range(start, end +1):
        if i % 2 ==1:
            print(i, end= ' ')

start_num = int(input('Baslangic ededi daxil edin: '))
end_num = int(input('Sonuncu ededi daxil edin: '))
odd_numbers(start_num, end_num)



# Tapsiriq 3.
def square(side, symbol, filled):
    if filled:
        for j in range(side):
            for i in range(side):
                print(symbol+" ", end="")
            print()
    else:
        print((symbol+" ")*side)
        for j in range(side-2):
            print(symbol+" ", end="")
            for i in range(side-2):
                print("  ", end="")
            print(symbol+" ", end="")
            print()
        print((symbol + " ") * side)

square(10, "1", True)



# Tapsiriq 5.
def hasil(start, end):
    if start>end:
        print("Error")
        return
    else:
        num = 1
        for i in range(start, end+1): # 5, 10 -> 5,6,7,8,9
            num *= i
        return num
result = hasil(2,7)
print(result)



# Tapsiriq 6.

def number(num):
    count_num = 0
    count_num += 1
        
input_number = input('Eded daxil edin: ')
print(number(input_number))
print(len(input_number))



# Tapsiriq 7.

def number(eded):
    if eded == eded[::-1]:
        return True
    else:
        return False

input_number = input('Eded daxil edin: ')
print(number(input_number))
"""



























































































































































































































