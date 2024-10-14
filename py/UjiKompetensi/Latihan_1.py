# Operator Penuggasan
print("a + b = c")
a = int(input("a: "))
b = int(input("b: "))
c = a + b

print("Hasil dari", a , "+", b, "adalah", c)

# Operator logika
print("Operator and perkalian")
angkake1 = int(input("Masukan nilai pertama : "))
angkake2 = int(input("Masukan nilai kedua   : "))

if angkake1 != 0 and angkake2 != 0 :
    jumlah = angkake1 * angkake2
    print("Haslnya adalah :", jumlah)
else :
    print("Nilai tidak boleh kosong")

print("")
# Operator Bitwise

a = 5  # 0b0101
b = 3  # 0b0011
hasil = a ^ b  # 0b0110
print(hasil)  # Output: 6
print("")

# Operator Identitas
a = [1, 2, 3]
b = a
c = a[:]

print(a is b)  # True, karena b adalah referensi yang sama dengan a
print(a is c)  # False, karena c adalah objek baru yang berisi salinan dari a
print(a is not c)  # True
print('')
# Operator Keaggotaan
ab = [1, 2, 3, 4, 5]
bb = 3
cb = 10

print(bb in ab)
print(cb in ab)