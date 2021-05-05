number = 50

# for i in range(0,5):
# 	print(i)
# else:
# 	print("hallo")

for i in range(0,40):
	print(i)
	if i is number:
		print('angka ditemukan',i)
		break
else:
	print('angka tidak ditemukan')

print("ini space di luar for")