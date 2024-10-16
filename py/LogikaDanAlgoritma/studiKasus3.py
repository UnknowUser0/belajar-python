def formatRupiah(rp):
    a = str(rp)
    if len(a) <= 3:
        return "Rp. " + a
    else:
        b = a[:-3]
        c = a[-3:]
        return formatRupiah(b) + "." +c

sewa3JamPertama = 6000
tarifBerikutnya = 5000
lamaPemakaian = int(input("Lama pemakaian (jam) :"))

if lamaPemakaian <= 3:
    biayaSewa = 6000 * lamaPemakaian
else:
    biayaSewa = 6000 * 3
    biayaSewaBerikutnya = 5000 * (lamaPemakaian - 3)
    biayaSewa = biayaSewa + biayaSewaBerikutnya

print(formatRupiah(biayaSewa))

