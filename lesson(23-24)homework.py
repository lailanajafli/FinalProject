# Tapsiriq.

import random
original_list = [[10, 12, 33, 34, 53, 12, 54, 62, 23, 11]]
random.shuffle(original_list)
for i in original_list:
    random.shuffle(i)
print(original_list)