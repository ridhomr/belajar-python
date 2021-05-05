import time
start_time = time.time()


print("Hello")
print("World")
print("Hello World")

print("Hallo Ridhomr")

# ini adalah commment

a = 10 # ini adalah comment
"""ini juga comment multiline"""
print(a)
for i in range(1,1000):
	a = 10

print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke
# ke bytecode
# cara mengcompile buka terminal dan ketikkan
# python -m py_compile Main.py
