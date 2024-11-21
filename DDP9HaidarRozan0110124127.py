#1. buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversike fahrenheit
#print(celcius_ke_fahrenheit(0)) output 32.0
#print(celciu_ke_fahrenheit(100)) ouput 212.0
print("------ mencari fahrenheit ke celcius ------")
def celcius_ke_fahrenheit(celcius):
    return (celcius * 9/5) + 32
#untuk mencetak value
print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))
#2. buat lah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan 
# false jika bilangan tersebut ganjil
#print(is_genap(4)) 
#print(is_genap(7))
print("\n----------- mencari bilangan genap ---------------")
def is_genap(angka):
    return angka % 2 == 0
#untuk mencetak value
print(is_genap(4)) 
print(is_genap(7))
#3. buatlah fungsi untuk melihat keterangan lulus atau gagal:
#nilai (80) lulus
#nilai(70) tidak lulus
print("\n---------- mencari keterangan nilai ---------------")
def nilai(nilaisiswa):
    if nilaisiswa >= 80:
        return "lulus"
    else:
        return "gagal"
# untuk mencetak value
print(nilai(80))
print(nilai(60))
#4. buatlah fungsi untuk menapilkan bilangan ganjil yang kurang argumen 
#bilangan (20)#1,3,5,7,9,11,13,15,17,19
print('\n-------- mencari bilangan ganjil 20 ---------')
def bilangan_ganjil(kurang_dari):
   for i in range(1, kurang_dari, 2):
       print(i, end=" ")
#untuk mencetak value
bilangan_ganjil(20)

