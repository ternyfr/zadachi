import random

list = []
n = 5
k = 0
while n > 0:
    list.append(random.randint(-10, 10))
    n -= 1
for i in range(0, len(list)-1):
    print(list[i], list[i+1], i)

print(list)
print(f"знак меняется {k} раз(-а)")