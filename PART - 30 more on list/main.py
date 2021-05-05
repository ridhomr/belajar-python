barang = ['kunci', 'gitar', 'motor', 'mobil', 'sepeda']
print(barang)

# beberapa method yang bisa digunakan untuk memanipulasi list
# method berfungsi menambah list
barang.append('sepeda')
print(barang)

barang.extend('dompet')
print(barang)

barang.insert(3,'dompet')
print(barang)

# method untuk menghitung anggota
jumlah_sepeda = barang.count('sepeda')
print('jumlah sepeda adalah :',jumlah_sepeda)

barang.remove('sepeda')
print(barang)

barang.reverse()
print(barang)


print("="*50)
stuff = barang.copy()
stuff.append('gelas')
print(stuff)


print(barang)