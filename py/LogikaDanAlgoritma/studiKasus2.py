A = int(input("A = "))
B = int(input("B = "))

if A+B < 10:
    C = A - B
else:
    C = A + B
    D = 2*C+B
    print(C, D)
