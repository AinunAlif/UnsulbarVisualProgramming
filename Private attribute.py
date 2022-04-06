class Product():
    __items = 10 # private
 
    def __init__(self, nama_barang):
        self.nama = nama_barang
 
    def harga_barng(self,harga_barang):
       hasil = self.__items * harga_barang
       return hasil
 
petasan = Product("petasan")
print(petasan.harga_barng(500))