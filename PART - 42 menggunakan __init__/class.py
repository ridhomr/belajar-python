# class
class mahasiswa():


	def __init__(self, input_nama, input_nim):
		self.nama = input_nama
		self.nim = input_nim

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)


	def ngoding(self, coding):
		print(self.nama, 'di kantor', coding)

# main program 

ridho = mahasiswa("ridho marhaban", 182102031)
print(ridho.nama)
print(ridho.nim)


ridho.belajar("python")
ridho.ngoding("sedang ngoding")
# ucup = mahasiswa()

# ridho.nama = "ridho marhaban"
# ucup.nama = "ucup ulala"
# print("\n ===================")

# ridho.belajar("dengan giat")
# ucup.ngoding("sedang ngoding")