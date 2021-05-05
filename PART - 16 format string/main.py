# format string

# contoh generic

# huruf
nama = "ridhomr"
str = "hello " + nama + " apa kabar"

print(str)

nama = "ridhomr"
format_str = f"hello, {nama}"

print(format_str)


# angka
angka = 2005.5
format_str = f"angka, {angka}"

print(format_str)


# boolean

boolean = True
format_str = f"nilai, {boolean}"
print(format_str)


# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)


# bilangan ribuan
angka = 20000000
format_str = f"ribuan = {angka:,}"
print(format_str)


# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.2f}"
print(format_str)


# menampilkan leading zero
angka = 2005.54321
format_str = f"desimal = {angka:010.2f}"
print(format_str)


# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10

format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus:+d}"

print(format_minus)
print(format_plus)


# memformat persen %
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)


# melakukan operasi aritmatika didalam placeholder
harga = 10000
jumlah = 5
format_string = f"harga total = Rp.{harga * jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary = {bin(angka)}" 
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)