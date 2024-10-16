def formatRupiah(rp):
    a = str(rp)
    if len(a) <= 3:
        return "Rp. " + a
    else:
        b = a[:-3]
        c = a[-3:]
        return formatRupiah(b) + "." +c

gajiPokok = 5000000
bonus20persen = 0.20
bonus10persen = 0.10

banyakProdukTerjual = int(input("Banyak Produk Terjual: "))
hargaSatuanProduk = int(input('Harga satuan produk :'))
omset = hargaSatuanProduk * banyakProdukTerjual

if banyakProdukTerjual > 100:
    bonus = omset * bonus20persen
else:
    bonus = omset * bonus10persen

gaji = gajiPokok + bonus
print(formatRupiah(int(gaji)))