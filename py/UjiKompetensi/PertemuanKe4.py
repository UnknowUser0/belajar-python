# input
print("PROGRAM HITUNG GAJI KARYAWAN")
namaKaryawan=input("Nama Karyawan : ")
golonganJabatan=int(input("Golongan Jabatan :"))
pendidikan=input("Pendidikan :")
jumlahJamKerja=int(input("Jumlah Jam Kerja: "))

# aplikasi
gajiPokok=300000

# hitung tunjangan jabatan
if golonganJabatan==1:
    tunjanganJabatan = 0.5 * gajiPokok
elif golonganJabatan==2:
    tunjanganJabatan = 0.10 * gajiPokok
elif golonganJabatan==3:
    tunjanganJabatan = 0.15 * gajiPokok
else :
    tunjanganJabatan = 0

# hitung Tunjangan Pendidikan
pendidikanUppercase = pendidikan.upper()
if pendidikanUppercase == "SMA":
    tunjanganPendidikan = 0.025 * gajiPokok
elif pendidikanUppercase == "D1":
    tunjanganPendidikan = 0.5 * gajiPokok
elif pendidikanUppercase == "D3":
    tunjanganPendidikan = 0.2 * gajiPokok
elif pendidikanUppercase == "S1":
    tunjanganPendidikan = 0.3 * gajiPokok
else:
    tunjanganPendidikan = 0

# Hitung Honor lembur
if jumlahJamKerja >= 8:
    honorLembur = (jumlahJamKerja - 8) * 3500
else:
    honorLembur = 0

totalGaji = gajiPokok + tunjanganJabatan + tunjanganPendidikan + honorLembur
totalGajiInt = int(totalGaji)

def format_rp(uang):
    a = str(uang)
    if len(a) <= 3:
        return a
    else:
        b = a[:-3]
        c = a[-3:]
        return format_rp(b) + '.' + c
# output
print("Karyawan yang bernama", namaKaryawan)
print("Honor yang diterima")
print("   Tunjangan Jabatan     Rp." + str(format_rp(int(tunjanganJabatan))))
print("   Tunjangan Pendidikan  Rp." + str(format_rp(int(tunjanganPendidikan))))
print("   Honor Lembur          Rp." + str(format_rp(int(honorLembur))))
print("                         —————————————— +")
print("   Total Gaji            Rp." + str(format_rp(totalGajiInt)))
