# a = 10, a adalah variabel dengan value 10

# tipe data: angka satuan (integer)

data_integer = 1
print("data : ",  data_integer)
print("- bertipe : ", type(data_integer))


# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))


# tipe data: huruf dengan petik (string)
data_str = "ridhomr"
print("data : ", data_str)
print(" - bertipe : ", type(data_str))


# tipe data: biner true or false (boolean)
data_bool = True 
print("data :", data_bool)
print(" - bertipe :", type(data_bool))


# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print(" - bertipe :", type(data_complex))


# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print(" - bertipe : ", data_c_double)