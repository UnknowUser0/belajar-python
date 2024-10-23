n = int(input("Masukan nilai antara 1-100: "))
karakter = input("Masukan karakter yang akan di print: ")

if n <= 100 :
    for i in range(n) :
        spasi = ' ' * (n - i)
        kata = karakter * (2 * i - 1)
        print(spasi + kata)