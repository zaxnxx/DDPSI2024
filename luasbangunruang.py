import math

def hitung_luas_kubus(sisi):
    hasil = (6 * (sisi ** 2))
    print(f"hasil luas kubus adalah {hasil}")  

def hitung_luas_tabung(radius, tinggi):
    hasil = (2 * math.pi * radius * (radius+tinggi))
    print(f"hasil luas tabung adalah {hasil}")  

def hitung_luas_balok(panjang, lebar, tinggi):
    hasil = (2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    print(f"hasil dari luas balok adalah {hasil}")

def hitung_luas_kerucut(r, s):
    hasil = (math.pi * r * (r + s))
    print(f"hasil luas kerucut adalah {hasil}")  



