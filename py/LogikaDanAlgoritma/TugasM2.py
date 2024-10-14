# variable
berat_telur = 5
harga_1kg_telur = 26000
tarif_angkot = 3500 #untuk sekali naik angkot
uang_yang_dibawa_ibu = 200000

#hitung
total_harga_telur_yang_dibeli_ibu = harga_1kg_telur * berat_telur
transport_pp = tarif_angkot * 2 #karena pp artinya pulang pergi berartinibu naik angkot 2x
sisa_uang_ibu = uang_yang_dibawa_ibu - total_harga_telur_yang_dibeli_ibu - transport_pp

# Format nilai mata uang menjadi Rp
def format_rp(uang):
    a = str(uang)
    if len(a) <= 3:
        return 'Rp '+ a
    else:
        b = a[:-3]
        c = a[-3:]
        return format_rp(b) + '.' + c

print("Sisa uang ibu adalah : "+ format_rp(sisa_uang_ibu))