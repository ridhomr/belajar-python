# list iterable
print("\nlist iterable")
gorengan = ['bakwan', 'ubi', 'tempe', 'tahu']

for g in gorengan:
	print(g)
	print(len(g))

print("\nstring sbg iterable")
# string sbg iterable
bakwan = 'bakwan'

for i in bakwan:
	print(i)

print("\nfor didalam for")
# for didalam for
# gorengan = ['bakwan', 'ubi', 'tempe', 'tahu']
buah = ['semangka', 'jeruk', 'apel', 'anggur']
sayur = ['bayam', 'kangkung', 'wortel', 'tomat']

daftar_belanja = [gorengan,buah,sayur]

for SubDataBelanja in daftar_belanja:
	print(SubDataBelanja)
	for komponen in SubDataBelanja:
		print(komponen)