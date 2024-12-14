from burung import *
from ular import *
from sapi import *
from ikan import *

# burung
k1 = burung("burung kakatua", "voer", "di darat", "bertelur", "pendek", "bisa meniru suara manusia")
lo1 = burung("lovebird", "biji bijian", "di darat", "bertelur", "paruh bengkok", "nyaring dan keras")

# ular
co1 = ular("ular cobra", "daging", "di darat", "bertelur", "berbisa", "cobra china")
w1 = ular("ular weling", "daging", "di darat", "bertelur", "tidak berbisa", "bungaurus fasciatus")

# sapi
b1 = sapi("sapi brahman", "rumput", "di darat", "melahirkan", "India", "800 - 1.000 kg")
l1 = sapi("sapi limosin", "rumput", "di darat", "melahirkan", "Prancis", "650 - 1.000 kg")

# ikan
c1 = ikan("ikan cupang", "cacing sutra", "di air", "bertelur", "Rp 15.000", "0,175 gram -m 0,307 gram")
g1 = ikan("ikan gurame", "daun talas", "di air", "bertelur", "Rp 42.000", "500 gram - 1 kg")

# cetak
k1.cetak_burung()
lo1.cetak_burung()
co1.cetak_ular()
w1.cetak_ular()
b1.cetak_sapi()
l1.cetak_sapi()
c1.cetak_ikan()
g1.cetak_ikan()

