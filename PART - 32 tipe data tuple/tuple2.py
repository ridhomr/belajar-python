import timeit

data_list = timeit.timeit(stmt="1,2,3,4,5,6,7,8,9", number=100000)
data_tuple = timeit.timeit(stmt="1,2,3,4,5,6,7,8,9", number=100000)


print("waktu untuk proses list :", data_list)
print("waktu untuk proses tuple :", data_tuple)