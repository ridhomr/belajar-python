# fungsi dengan return value

def kuadrat(argument):
	total = argument**2
	print("nilai kuadrat dari", argument, "adalah :", total)
	return total

a = kuadrat(4)
print(a)

print("+"*100)

# fugsi dengan return value dengan multiple arguments
def tambah(argumen1, argumen2):
	total = argumen1 + argumen2
	print(argumen1,"+",argumen2,"=", total)
	return total

def kali(argumen1, argumen2):
	total = argumen1 * argumen2
	print(argumen1,"x",argumen2,"=", total)
	return total

	
b = kali(3,tambah(3,4))	

print(b)
