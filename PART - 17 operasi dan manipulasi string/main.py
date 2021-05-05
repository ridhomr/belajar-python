# operasi dan manipulasi string

# menyambung string(concatenate)
nama_pertama = "ridho"
nama_tengah = "marhaban"
nama_akhir = "ganteng"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

# operator untuk string
# mengecek apakah ada komponen char / string di string
d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("string " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wkwk"*10)
print(10* "wkwk")

# indexing
print("index ke 11 : " + nama_lengkap[11])
print("index ke -1 : " + nama_lengkap[-1])
print("index ke -0[0,3]:" + nama_lengkap[0:3])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
print("paling besar : " + max(nama_lengkap))

# operator dalam bentuk method
data = "otong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))