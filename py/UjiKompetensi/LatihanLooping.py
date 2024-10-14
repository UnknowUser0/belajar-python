print('''
GEROBAK FRIED CHICKEN
--------------------------------------
Kode JenisPotong Harga
--------------------------------------
D       Dada     Rp. 2500
P       Paha     Rp. 2000
S       Sayap    Rp. 1500
--------------------------------------
''')

dada = 2500
paha = 2000
sayap = 1500
pajak = 0.1

banyakPesanan = int(input("Banyak Jenis: "))
no = 1
#iterasi
for i in range(banyakPesanan):
    kodePotong = input("Kode Potong [D/P/S] : ")
    banyakPotong = int(input("Banyak Potong: "))
    no = no + 1
    if kodePotong.upper() == "D":
        jenisPotong = "Dada"
        hargaSatuan = "Rp.2.500"
        jumlahHarga = 2500 * banyakPotong
    elif kodePotong.upper() == "P":
        jenisPotong = "Paha"
        hargaSatuan = "Rp.2.000"
        jumlahHarga = 2000 * banyakPotong
    elif kodePotong.upper() == "S":
        jenisPotong = "Sayap"
        hargaSatuan = "Rp.1.500"
        jumlahHarga = 1500 * banyakPotong
    else:
        print("Kode Potong salah atau tidak ada")

    # output
    print("""
    GEROBAK FIRED CHICHEN 
    ------------------------------------- 
    No. Jenis   Harga   Bayak   Jumlah  
        Potong  Satuan  Beli    Harga   
    -------------------------------------
    %i  %s      %s      %i      Rp.%i
    """ % (no,jenisPotong,banyakPotong,jumlahHarga))
