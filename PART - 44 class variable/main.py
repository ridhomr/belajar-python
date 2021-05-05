class mahasiswa():

	jumlah_mahasiswa = 0


	def __init__(self, input_nama, input_nim):
		self.nama = input_nama
		self.nim = input_nim

		mahasiswa.jumlah_mahasiswa += 1



ridho = mahasiswa("ridho marhaban", 182102031)
ucup = mahasiswa("ucup aja", 18219371)
lala = mahasiswa("lala azahra", 213817414)

print(mahasiswa.jumlah_mahasiswa)






# ridho.kegemarain = "membaca"


# print(mahasiswa.jurusan)
# print(ridho.jurusan)
# print(ucup.jurusan)

# print(mahasiswa.__dict__)
# print(ridho.__dict__)