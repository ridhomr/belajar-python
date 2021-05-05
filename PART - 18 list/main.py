data = [1,4,9,16,25,36,49,64]

# mengakses list
subdata1 = data[3]
subdata2 = data[-3]


# memotong list
subdata3 = data[0:4]
subdata4 = data[-4:]
data2 = [100,200,300,400,500,600]


# menambah list
data3 = data + data2
data[4] = 87


# mengcopy list ke variabel baru
a = data[:] 
a[7] = 87


# merubah content list dengan menggunakan metode slicing
data[3:5] = [11,12]


# list dalam list
x = [data,data2]


# mengakses list dalam multidimensional list
y =x[1][4]


# method untuk list
data.append(30)


# function yang bisa kita gunakkan kepada list
panjang_list = len(data)
print(data)
print(panjang_list)

