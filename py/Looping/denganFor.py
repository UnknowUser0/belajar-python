# Program untuk menemukan jumlah bilangan

# List Number
numbers = [1,2,3,4,5,6,7,8,9,10]

# membuat variable kosong
sum = 0

# iteration
for each in numbers:
    sum = sum + each

# out
print("Jumlah semuanya : ", sum)

# Dengan range()
prodi = ['Informatika', 'Sistem Informatika', 'Ilmu Komputer']

# iterasi
for i in range(len(prodi)):
    print("Saya suka", prodi[i])