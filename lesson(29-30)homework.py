# Tapsiriq

list = []
for i in range(3):
    list_2 = []
    for j in range(3):
        j = int(input(f"Enter number is pocked [ "+str(i) +"] ["+str(j)+"] enter the number"))
        list_2.append(j)
    list.append(list_2)
print('Matrix is .....')

for i in range(3):
    for j in range(3):                                                                               #men yazan duzdu 12
        print (list[i][j],end= " ")
    print()
t = [[0,0,0], [0,0,0], [0,0,0]]
for i in range(3):
    for j in range(3):
        t[i][j] = list[j][i]
print('Transpose of Matrix is...')
for i in range(3):
    for j in range(3):
        print(t[i][j], end=" ")
    print()





00 01 02
10 11 12
20 21 22

'''
'''
matrix = [[12, 34, 23], [45, 56, 78], [91, 55, 21]]
for element in matrix:
    print(element)

transposed_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]                       # muellime yazan

print(transposed_matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        transposed_matrix[j][i] = matrix[i][j]

for element in transposed_matrix:
    print(element)






















