class Animal:
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def makan(self):
        print(f"{self.name}sedang makan{self.makanan}")
        
    def tidur(self):
        print(f"{self.name}sedang tidur")

class Gajah(Animal):
    def makanan(self):
        print("rumput")

class hidup(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, hidung):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.hidung=hidung
        
    def telinga(self):
        print(f"{self.name}telinga dan hidung yang panjang")
        
class Kucing(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, kumis):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.kumis = kumis
        
    def memiliki_kumis(self):
        print(f"{self.name}memiliki kumis yang panjang")
        
class kupu_kupu(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, warna):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna = warna
        
    def terbang(self):
        print(f"{self.name}terbang di udara")
        
