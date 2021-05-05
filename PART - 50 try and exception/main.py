
# def pembagian(a,b):
# 	return a/b


# penyebut = int(input("masukkan angka penyebut\n"))
# pembilang = int(input("masukkan angka pembilang\n"))

# print(pembagian(penyebut,pembilang))


# a = 1/0 # error ZeroDivisionError

# try:
# 	a = 1/0
# except:
# 	print("error pembagi nol")


# print("akhir program")

print("ini adalah program pembagian\n")

# hasil = 1/0

while True:
	try:
		import panda # ImportError (tidak ada modul panda)
		penyebut = int(input("masukkan angka penyebut:"))
		pembilang = int(input("masukkan angka pembilang:"))
		hasil = penyebut / pembilang
		break
	except ValueError:
		print("yang anda masukkan bukan angka")
	except ZeroDivisionError:
		print("yang anda masukkan adalah pembagian nol")
	except Exception as err:
		print(err)
	except ImportError:
		print("tidak ada modulnya")
print("berhasil, hasil pembagian adalah: ", hasil)

# TYPE OF EXCEPTION ERRORS :
# 1. IOError
# 2. ImportError
# 3. ValueError
# 4. ZeroDivisionError
# 5. KeyboardInterupted
# 6. EOFError