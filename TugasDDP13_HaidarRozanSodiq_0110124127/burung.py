from Animalparents import *
class burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_paruh, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_paruh= jenis_paruh
        self.bunyi = bunyi

    def cetak_burung(self):
        print("Nama\t\t:", self.nama,
            "\nmakanan\t\t:",self.makanan,
            "\nhidup \t\t:",self.hidup,
            "\nberkembang biak\t:", self.berkembang_biak,
            "\njenis \t\t:", self.jenis_paruh,
            "\nbunyi \t\t:", self.bunyi,
            "\n----------------------------")