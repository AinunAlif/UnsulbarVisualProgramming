class Kelas_A():
	def __init__(self, nama, nim, matakuliah):
		self.nama = nama
		self.nim = nim
		self.matakuliah = matakuliah
		
	def cek_id_kelas(self):
		print('Nama:',self.nama, '\nNim:',self.nim, '\nMatakuliah:',self.matakuliah)
		
kelas1 = Kelas_A('Ainun Alif', 'D0219417', 'Pemrograman Visual')

kelas1.cek_id_kelas()