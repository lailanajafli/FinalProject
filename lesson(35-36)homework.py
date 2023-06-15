# Tapsiriq 1.
'''
tuple1 = (1, 5, 12, 9)
tuple2 = (4, 6, 1, 20)
tuple3 = (8, 11, 3)

all = tuple1 + tuple2 + tuple3

for i in all:
    if all.count(i) != 1:
        print(i)
'''
# Tapsiriq 2.
'''
tuple1 = (1, 5, 12, 9)
tuple2 = (4, 5, 1, 20)
tuple3 = (8, 1, 5)

all = tuple1 + tuple2 + tuple3

for i in all:
    if all.count(i) == 1:
        print(i)
'''

# Tapsiriq 3.
'''
tuple1 = (7, 5, 3, 9)
tuple2 = (4, 5, 1, 20)
tuple3 = (7, 5, 3)
for i in tuple1, tuple2, tuple3:
    if tuple1[i] == tuple2[i] == tuple3[i]:
        print(tuple1[i])
    else:
        print('Indexleri beraber olan element yoxdur')
'''

