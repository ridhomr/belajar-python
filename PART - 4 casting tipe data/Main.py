# belajar casting
# merubah dari satu tipe ke tipe lain

# tipe data : int, str, float, bool
## INTEGER
print("=====INT=====")
data_int = 9;
print("data", data_int, ", type", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0

print("data", data_float, ", type",type(data_float))
print("data", data_str, ", type",type(data_str))
print("data", data_bool, ", type",type(data_bool))


# print("====coba casting int====")
# data_int = 99;
# print("data", data_int, ", type", type(data_int))

# data_float = float(data_int)
# data_str = str(data_int)
# data_bool = bool(data_int)

# print("data", data_float, ", type", type(data_float))
# print("data", data_str, ", type", type(data_str))
# print("data", data_bool, ", type", type(data_bool))


## FLOAT
print("=====FLOAT=====")
data_float = 0;
print("data", data_float, ", type", type(data_float))

data_float = float(data_float) # akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai int = 0

print("data", data_int, ", type",type(data_int))
print("data", data_str, ", type",type(data_str))
print("data", data_bool, ", type",type(data_bool))


# print("====coba casting data float====")
# data_float = 30.9;
# print("data", data_float, ", type", type(data_float))

# data_int = int(data_float)
# data_str = str(data_float)
# data_bool = bool(data_float)

# print("data", data_int, ", type", type(data_int))
# print("data", data_str, ", type", type(data_str))
# print('data', data_bool, ", type", type(data_bool))



## BOOLEAN
print("=====BOOLEAN=====")
data_bool = True;
print("data", data_bool, ", type", type(data_bool))

data_float = float(data_bool) # akan dibulatkan ke bawah
data_str = str(data_bool)
data_bool = bool(data_bool) # akan false jika nilai int = 0

print("data", data_int, ", type",type(data_int))
print("data", data_str, ", type",type(data_str))
print("data", data_float, ", type",type(data_float))


print("====coba casting data boolean====")
data_bool = True;
print("data", data_bool, ", type", type(data_bool))

data_int = int(data_bool)
data_str = str(data_str)
data_float = float(data_float)
print("data", data_float, ", type", type(data_float))
print("data", data_str, ", type", type(data_str))
print("data", data_int, ", type", type(data_int))



## STRING
print("=====STRING=====")
data_str = "False";
print("data", data_str, ", type", type(data_str))

#data_int = int(data_str) # str harus angka
#data_float = float(data_str) # str harus angka
data_bool = bool(data_str) # akan false jika nilai str = kosong

#print("data", data_int, ", type",type(data_int))
#print("data", data_float, ", type",type(data_float))
print("data", data_bool, ", type",type(data_bool))

print("====casting data str====")
data_str = "10"

print("data", data_str, ", type", type(data_str))

data_int = int(data_str)
print("data", data_int, ", type", type(data_int))