class mahasiswa():
    jurusan = "Pemrograman Visual"
 
    def __init__(self, input_nama):
        self.nama = input_nama # public
 
alif = mahasiswa("Ainun Alif")
 
print(mahasiswa.jurusan)
print(alif.jurusan)