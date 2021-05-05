# operasi logika atau boolean

# not, or, and, xor

print("====NOT====")

a = False
c = not a
print('nilai data a =', a)

print('-------------------NOT')

print('data c =', c)


# OR (jika salah satu true maka hasil nya true)
print("====OR====")

a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)



# and (jika 2 buah true, maka hasil true)
print("====AND====")

a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)


# xor (jika 2 buah nilai sama maka output = false, jika 2 buah nilai berbeda maka bernilai true)
print("====AND====")

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, 'XIR', b, '=', c)

