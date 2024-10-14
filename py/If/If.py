# Bilanagan positif, tampilkan pesan


angka = 5
if angka > 0 :
  print(angka, "adalah bilangan positif.")
  
angka = -1
# berikut tidak di execute karena False
if angka > 0 :
  print(angka, "adalah bilangan positif.")

number = int(input("Masukan nilai : "))
if number > -1:
  print(number, "adalah positif")
else:
  print(number,"adalah Negatif")