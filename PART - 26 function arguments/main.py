# fungsi dengan menggunakan argumen sederhana
def siswa(nama):
	print("siswa ini bernama :", nama)

siswa("mario")

# fungsi dengan menggunakan keywords arguments
def guru(nama, pelajaran):
	print("guru ini bernama :", nama)
	print("mengajar:", pelajaran)

guru(nama="lala", pelajaran="fisika")

guru(pelajaran="seni", nama="etika")

guru("seni","raihan") # contoh yang salah

# fungsi dengan menggunakan default arguments

def penjaga_sekolah(nama, shift="siang", alamat="jogja"):
	print("penjaga sekolah ini bernama :", nama)
	print("shiftnya jam :", shift)
	print("alamatnya di :", alamat)

penjaga_sekolah("entis")
penjaga_sekolah("maman", shift="malam")
penjaga_sekolah("joko", alamat="banten")
#penjaga_sekolah(shift="malam", alamat="bantul") #error karena default argument