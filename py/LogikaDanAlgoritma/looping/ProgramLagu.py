n = int(input("Masukan banyak looping: "))
print("Tek kotek kotek kotek, anak ayam turun berkotek")
for i in range(n):
    if n == 1:
        print("anak ayam turunlah 1 mati satu tinggallah induknya")
        break
    jumlah = n
    n = n - 1
    print(f"anak ayam turunlah {jumlah} mati satu tinggallah {n}")
