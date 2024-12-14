from Animalparents import *
class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, harga, berat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.harga=harga
        self.berat=berat

    def cetak_ikan(self):
        print("Nama\t\t:", self.nama,
            "\nmakanan\t\t:",self.makanan,
            "\nhidup \t\t:",self.hidup,
            "\nberkembang biak\t:", self.berkembang_biak,
            "\nharga\t\t:", self.harga,
            "\nberat\t\t:", self.berat,
            "\n--------------------------")