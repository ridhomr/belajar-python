# teknik looping

nama_band = ['payung teduh', 
			 'fourtwnty',
			 'dialog dini hari',
			 'parahyena']

# iterasi = 0;

# for band in nama_band:
# 	print("no:", iterasi, 'nama_band', band)
# 	iterasi += 1



kumpulan_lagu = ['akad', 'zona nyaman', 'daun', 'reggae']

print("\n ========")
# enumerate
for i,band in enumerate(nama_band):
	print(i, ":", band)



print("\n ========")
# zip (menggabungkan list)
for band,lagu in zip(nama_band,kumpulan_lagu):
	print(band, "menyanyikan lagu berjudul:", lagu)


print("\n ========")
# set
playlist = {'scorpio', 'avenged', 'dream'}

for lagu in sorted(playlist):
	print(lagu)


print("\n ========")
# dictionary
playlist2 = {'payung teduh': 'akad', 
			 'fourtwnty':'four',
			 'dialog dini hari':'dialog',
			 'parahyena':'yena',
			 'roma irama':'roma'}

for i,yy in playlist2.items():
	print(i, "lagunya:", yy)

for i in reversed(range(1,10)):
	print(i)