bilangan = int(input("Masukan bilangan bulat 1 - 100: "))

if bilangan > 100:
    print("Bilangan lebih dari 100")
else:
    for i in range(bilangan):
        i = i + 1
        bintang = "* "
        bintang = bintang * i
        print(bintang)