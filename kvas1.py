list = []
n = int(input("введи длину будущего списка, больше 1:"))
if n > 1:
    while n > 0:
        a = int(input("введите число:"))
        list.append(a)
        n -= 1
print(min(list))
list.remove(min(list))
print(min(list))