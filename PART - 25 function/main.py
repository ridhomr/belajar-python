# cara mendefinisikan fungsi
def fungsi():
	print("ini adalah fungsi")

# memanggil fungsi
fungsi()
fungsi()
fungsi()
fungsi()



print("\n fungsi sederhana")
# membuat fungsi sederhana
def suara_ayam():
	print("kukuruyuk")

def harga_ayam():
	suara_ayam()
	print("harga ayam per 1 kg adalah Rp.20000")

# membuat fungsi dengan input argumen
def hargatotalayam(kg):
	# suara_ayam()
	harga = 20000
	hargatotal = kg*harga
	print("harga", kg,"ayam adalah :", hargatotal)


harga_ayam()
hargatotalayam(3)
hargatotalayam(0.5)
hargatotalayam(1)
hargatotalayam(9)