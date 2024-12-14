from Animalparents import *
class sapi(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berasal_dari, berat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berasal_dari = berasal_dari
        self.berat = berat

    def cetak_sapi(self):
        print("Nama\t\t:", self.nama,
            "\nmakanan\t\t:",self.makanan,
            "\nhidup \t\t:",self.hidup,
            "\nberkembang biak\t:", self.berkembang_biak,
            "\nberasal dari\t:", self.berasal_dari,
            "\nbunyi \t\t:", self.berat,
            "\n----------------------------")