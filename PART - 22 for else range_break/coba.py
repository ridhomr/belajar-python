angka = 41

for a in range(0, 40):
	print(a)
	if a is angka:
		print("angka ditemukan", a)
		break
else:
	print("angka tidak ditemukan")