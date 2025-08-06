# ДЗ 4.3. Список із 3 елементів

import random

# lst = [1, 2, 3, 4, 5, 6, 7, 9]
# lst = [1, 1, 2, 1]
# lst = [6, 3, 7]

lst = []

for i in range(random.randint(3, 10)):
    lst.append(random.randint(-50, 50))

new_lst = []

for i in [0, 2, -2]:
    new_lst.append(lst[i])

print(lst, new_lst, sep='\n')