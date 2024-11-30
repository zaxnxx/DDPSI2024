import math

def tambah(angka1, angka2):
    hasil = (angka1 + angka2)
    print(f"hasil dari {angka1} ditambah {angka2} adalah {hasil}")
    
def kurang(angka1, angka2):
    hasil = (angka1 - angka2)
    print(f"hasil dari {angka1} dikurang {angka2} adalah {hasil}")

def kali(angka1, angka2):
    hasil = (angka1 * angka2)
    print(f"hasil dari {angka1} dikali {angka2} adalah {hasil}")

def bagi(angka1, angka2):
    hasil = (angka1 / angka2)
    print(f"hasil dari {angka1} dibagi {angka2} adalah {hasil}")

def pangkat(angka1, angka2):
    hasil = (angka1 ** angka2)
    print(f"hasil dari {angka1} dipangkat {angka2} adalah {hasil}")

def akar(angka):
    hasil = (math.sqrt(angka))
    print(f"hasil dari akar {angka} adalah {hasil}")

