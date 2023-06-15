secim = int(input('Secim daxil edin: (1-10) ' ))
if secim == 1:
    for i in range(5):
        for j in range(5):
            if j >= i:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 2:
    for i in range(5):
        for j in range(5):
            if j <= i:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 3:
    for i in range(5):
        for j in range(5):
            if j >= i and j + i <= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 4:
    for i in range(5):
        for j in range(5):
            if i >= j and j + i >= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 5:
    for i in range(5):
        for j in range(5):
            if i >= j and j + i >= 4 or j >= i and j + i <= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 6:
    for i in range(5):
        for j in range(5):
            if i >= j and j + i <= 4 or j >= i and j + i >= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 7:
    for i in range(5):
        for j in range(5):
            if i >= j and j + i <= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 8:
    for i in range(5):
        for j in range(5):
            if j >= i and j + i >= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 9:
    for i in range(5):
        for j in range(5):
            if j + i <= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()

elif secim == 10:
    for i in range(5):
        for j in range(5):
            if j + i >= 4:
                print('*', end='\t')
            else:
                print(end='\t')
        print()
else:
    print('Zehmet olmasa (1-10) araliginda secim daxil edin:')