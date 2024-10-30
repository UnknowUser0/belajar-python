def fibonancy(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonancy(n-1) + fibonancy(n-2))

x = int(input("Masukan Batas Deret Bilangan Fibonacci : "))
print("Deret Fibonacci")
for i in range(x):
    print(fibonancy(i))