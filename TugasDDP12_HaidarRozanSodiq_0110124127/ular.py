from Animalparents import *
class ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, berbisa, jenis):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.berbisa = berbisa
        self.jenis= jenis
    
    def cetak_ular(self):
        print("Nama\t\t:", self.nama,
            "\nmakanan\t\t:",self.makanan,
            "\nhidup \t\t:",self.hidup,
            "\nberkembang biak\t:", self.berkembang_biak,
            "\nberbisa/tidak\t:", self.berbisa,
            "\njenis \t\t:", self.jenis,
            "\n---------------------------")
        

