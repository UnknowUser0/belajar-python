import pandas as pd

list_nim=[]
list_nama=[]
list_uts=[]
list_uas=[]
list_total=[]

loop = 2
for i in range(loop):
    print('data ke -', str(i+1))
    list_nim.append(input("Nim : "))
    list_nama.append(input("Nama : "))
    list_uts.append(int(input("Nilai UTS: ")))
    list_uas.append(int(input("Nilai UAS : ")))
    
for i in range(loop):
    list_total.append((list_uts[i] + list_uas[i]) / 2)
    
tamu = {
    "Nim" : list_nim,
    "Nama Lengkap" : list_nama,
    "Nilai UTS" : list_uts,
    "Nilai UAS" : list_uas,
    "Rata-rata" : list_total
}
data_tamu = pd.DataFrame(tamu)

print("===================Daftar Nilai================")
print(data_tamu)
print("===============================================")
