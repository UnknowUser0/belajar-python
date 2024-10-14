# Operator Nama dan Fungsi Contoh
# + Penjumlahan, menjumlahkan 2 buah operand a + b
# – Pengurangan, mengurangkan 2 buah operand a – b
# * Perkalian, mengalikan 2 buah operand a * b
# / Pembagian, membagi 2 buah operand a / b
# ** Pemangkatan, memangkatkan bilangan a ** b
# // Pembagian bulat, menghasilkan hasil bagi tanpa koma a // b
import os

# nilai1 = 10
# nilai2 = 8
# penjumlahan = nilai1 + nilai2
# print(nilai1, "+", nilai2, "=", penjumlahan)
# pengurangan = nilai1 - nilai2
# print(nilai1, "-", nilai2, "=", pengurangan)
# perkalian = nilai1 * nilai2
# print(nilai1, "x", nilai2, "=", perkalian)
# pembagian = nilai1 / nilai2
# print(nilai1, "/", nilai2, "=", pembagian)
# pemangkatan = nilai1 ** nilai2
# print(nilai1, "**", nilai2, "=", pemangkatan)
# pembagian_bulat = nilai1 // nilai2
# print(nilai1, "//", nilai2, "=", pembagian_bulat)

os.system('clear')
nilai1 = int(input("Masukan Nilai Pertama : "))
nilai2 = int(input("Masukan Nilai Kedua   : "))
penjumlahan = nilai1 + nilai2
print(nilai1, "+", nilai2, "=", penjumlahan)
pengurangan = nilai1 - nilai2
print(nilai1, "-", nilai2, "=", pengurangan)
perkalian = nilai1 * nilai2
print(nilai1, "x", nilai2, "=", perkalian)
pembagian = nilai1 / nilai2
print(nilai1, "/", nilai2, "=", pembagian)
pemangkatan = nilai1 ** nilai2
print(nilai1, "**", nilai2, "=", pemangkatan)
pembagian_bulat = nilai1 // nilai2
print(nilai1, "//", nilai2, "=", pembagian_bulat)