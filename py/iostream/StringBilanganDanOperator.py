var1 = 'Hello Uler'
var2 = "Coding dengan Uler"
print(var1)
print(var2)
print("var1[0]: ", var1[0])
print("var2[1:6]: ", var2[:6])

# menggubah data tipe string
var3 = var1[:6]
print(var1)
print(var3 + "World")

# Menggabungkan string
# Note untuk menggabungkan dapat menggunakan + dan , dimana
# jika menggunakan , maka terhitung spasi
print("var1 + var2 : ", var1 , "+ " + var2)
# String dapat di kalikan dengan * tetapi harus dikali dengan int karena int dladalah nilai
print("var1 * 5 :", var1 * 5)

# len berfungsi untuk mengetahui panjang sebuah string
print("panjang var1 :", len(var1))

# untuk mencetak karakter escape
print('''He said, "What's there?"''')
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")

# Karakter Escape Deskripsi
# \newline Backslash dan newline diabaikan
# \\ Backslash
# \’ Kutip tunggal
# \” Kutip ganda
# \a ASCII bel
# \b ASCII backscape
# \f ASCII formfeed
# \n ASCII linefeed
# \r ASCII carriage return
# \t ASCII tab horizontal
# \v ASCII tab horizontal
# \ooo karakter dengan nilai oktal oo
# \xHH karakter dengan nilai heksadesimal HH

print("ini adalah baris pertama \n Dan ini baris ke 2")
print("Ini adalah \x48\x45\x58")

# Untuk mengabaikan karakter escape maka dapat menambahkan r atau R
print("This is \x61 \ngood example")
print(r"This is \x61 \n good example")

# Placeholder
# menggunakan posisi default
default_order = "{}, {} dan {}".format("Sky", "X", "Unknow")
print('\n--- Urutan default ---')
print(default_order)

# Menggunakan  argument posisi
positional_order = "{1}, {0} dan {2}".format("Sky", "X", "Unknow")
print('\n--- Urutan berdasarkan posisi ---')
print(positional_order)

# format integer
print("{0} bila diubah jadi biner menjadi {0:b}".format(12))

# format float
print("Format eksponensial: {0:e}".format(1566.345))

# pembulatan
print("Sepertiga sama dengan: {0:.3f}".format(1/3))

# Meratakan string
print("|{:<10}|{:^10}|{:>10}|".format('beras', 'gula', 'garam'))

# contoh placeholder yang sering digunakan yaitu dengan %
x = 12.3456789
print("Nilai x = %3.2f" %x)
print("Nilai x = %3.4f" %x)

# Contoh penggunaan metode
print("Universitas Bina Sarana Informatika".lower())
print("Universitas Bina Sarana Informatika ".upper())
print("I love programming in Python".split())
print("I love Python".startswith("I"))
print("Saya belajar Python".endswith("on"))
print(' '.join(['I', 'love', 'you']))
print("Belajar Java di BSI".replace('Java', 'Python'))
