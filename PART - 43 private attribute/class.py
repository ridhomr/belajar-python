# class
class mahasiswa():

	jurusan = "teknik informatika"
	__nilai = 0 # private

	def __init__(self, input_nama, input_nim):
		self.nama = input_nama # public
		self.nim = input_nim	# public

	def uts(self, input_nilai):
		self.__nilai += input_nilai

	def uas(self, input_nilai):
		self.__nilai += input_nilai

	def cek_status(self):
		if self.__nilai == 50:
			print(self.nama, "tidak lulus")

		else:
			print(self.nama, "lulus")

# main program 

ridho = mahasiswa("ridho marhaban", 182102031)
ucup = mahasiswa("ucup", 32409234)


ridho.uts(10)
ridho.uas(50)

ridho.cek_status()


ucup.uts(30)
ucup.uas(20)

ucup.cek_status()