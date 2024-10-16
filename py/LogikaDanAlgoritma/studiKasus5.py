def formatRupiah(rp):
    a = str(rp)
    if len(a) <= 3:
        return "Rp. " + a
    else:
        b = a[:-3]
        c = a[-3:]
        return formatRupiah(b) + "." +c

gp = int(input("Masukan Gaji Pokok : "))
tjg = gp * 0.20
jk = int(input("Masukan Jam Kerja : "))

if jk > 200:
    lm = 20000 * (jk - 200)
else:
    lm = 0
gaji = gp + tjg + lm
pajak = gaji * 0.10
totalGaji = gaji - pajak

print(formatRupiah(int(totalGaji)))