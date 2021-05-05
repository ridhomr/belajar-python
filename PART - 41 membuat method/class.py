# class
class mahasiswa():
	nama = 'lala'

	def belajar(self, kondisi):
		print(self.nama,'sedang belajar', kondisi)


	def ngoding(self, coding):
		print(self.nama, 'di kantor', coding)

# main program 

ridho = mahasiswa()
ucup = mahasiswa()

ridho.nama = "ridho marhaban"
ucup.nama = "ucup ulala"
print("\n ===================")

ridho.belajar("dengan giat")
ucup.ngoding("sedang ngoding")