hargaperkg = int(input("Harga perkilo : "))
beratpembelian = int(input("Berat dibeli : "))

hargayangharusdibayar = hargaperkg * beratpembelian

# Format nilai mata uang menjadi Rp
def format_rp(uang):
    a = str(uang)
    if len(a) <= 3:
        return 'Rp '+ a
    else:
        b = a[:-3]
        c = a[-3:]
        return format_rp(b) + '.' + c

print("Harga yang harus dibayar :", format_rp(hargayangharusdibayar))
