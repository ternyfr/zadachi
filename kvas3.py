def chisla():
    a = int(input("первое число:"))
    b = int(input("второе число:"))
    c = []
    if a >= b:
        for i in range(a, b, -1):
            if i % 2 == 0:
                c.append(i)
            print(i, end=" ")
    else:
        for i in range(a, b):
            if i % 2 == 0:
                c.append(i)
            print(i, end=" ")
chisla()