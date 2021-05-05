list = [1,2,3,4,5]
tuple = (1,2,3,4,5)
set = {1,2,3,4,5}

print(type(list))
print(type(tuple))
print(type(set))


print("\nbelajar dict")

# dictionary
number1 = {"id":101, "nama":"ridhomr", "Nim":182102031, "status":"member"}

number2 = {"id":220, "nama":"ujang", "pekerjaan":"ngoding", "status":"mahasiswa"}

memberlist = {101:number1, 220:number2}

print(memberlist[101])
print(memberlist[220])



# print(number1["status"])
# print(number1.keys())
# print(number1.values())
# print(number1.items())