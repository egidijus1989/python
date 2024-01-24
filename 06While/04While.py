# 1
# 1 2
# 1 2 3
# 1 2 3 4
#antra uzduotis
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(1, 11):
    for j in range(1, i + 1):
        print(j, end=(' '))
    print()
for i in range(10, 0, -1):
    for j in range(1, i):
        print(j, end=(' '))
    print()