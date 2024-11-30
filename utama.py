import hitung, luasbangundatar as lb, luasbangunruang as lbr

# menghitung angka 
print("-------menghitung angka---------")
print(hitung.tambah(3,4))
print(hitung.kurang(3,4))
print(hitung.kali(3,4))
print(hitung.bagi(20,5))
print(hitung.pangkat(20,5))
print(hitung.akar(100))

# menghitung luas bangun datar
print("\n-------menghitung luas bangun datar---------")
print(lb.hitung_luas_segitiga(5,6))
print(lb.hitung_luas_persegi(6))
print(lb.hitung_luas_persegipanjang(5,6))
print(lb.hitung_luas_lingkaran(30))
print(lb.hitung_luas_trapesium(8,8,9))

# menghitung luas bangun ruang
print("\n-------menghitung luas bangun ruang---------")
print(lbr.hitung_luas_kubus(9))
print(lbr.hitung_luas_kerucut(8,9))
print(lbr.hitung_luas_tabung(8,9))
print(lbr.hitung_luas_balok(10,9,10))