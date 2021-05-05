print("\nscope local")
# scope variabel : local

nama_kucing = "dian"

def rubah_nama(namabaru):
	nama_kucing = namabaru
	print("rubah nama kucing :", nama_kucing)

rubah_nama("belang")

print("nama kucing saya menjadi :",nama_kucing)


print("\nscope global")
# scope variabel : global

nama_kucing = "dian"
makanan = "ikan goreng"

def rubah_nama(namabaru):
	global nama_kucing
	nama_kucing = namabaru # variabel global

	# nama = namabaru  -->  # variabel lokal

	print("rubah nama kucing :", nama_kucing)


def makanan_kucing(makanan, nama):
	global nama_kucing, makanan_kucing
	nama_kucing = nama 
	makanan_kucing = makanan


rubah_nama("belang")

makanan_kucing("rendang", "alex")

print("nama kucing saya menjadi :",nama_kucing, "dan makanan", makanan_kucing)