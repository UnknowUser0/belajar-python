# Python

print("			TOKO MAINAN ANAK		")
print("		********************************")

nama_pembeli = input("Masukan Nama Pembeli : ")
kode_mainan = input("Masukan Kode Mainan : ")
harga_barang = int(input("Masukan Harga : "))
jumlah_unit = int(input("Masukan Jumlah Beli : "))
total_harga = int(jumlah_unit) * int(harga_barang)

print("===============================================")

print("Nama Pembeli =", nama_pembeli)
print("Kode Mainan  =", kode_mainan.upper())
print("Harga        =", harga_barang)
print("Jumlah Beli  =", jumlah_unit)
print("Total        =", total_harga)
