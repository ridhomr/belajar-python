# operasi assignment
# yang dapat dilakukan dengan penyingkatan
# operasi di tambah dengan assignment

a = 5 # ini adalah assignment
print('nilai a :', a)

a += 1 # artinya adalah a = a + 1
print("nilai a menjadi =", a)

a -= 2
print("nilai a -= 2, nilai a menjadi", a)

a *= 5
print("nilai a *= 5, nilai a menjadi", a)

a /= 2
print("nilai a /= 2, nilai a menjadi", a)

b = 10 
print("\n nilai b =", b)

# modulus
b %= 3
print("nilai b %= 3, nilai b menjadi ", b)

# pembagian
b //= 3
print("nilai b //= 3, nilai b menjadi ", b)

a = 5
print("nilai a //= 3, nilai b menjadi", b )

# pangkat eksponen
a = 5
print("nilai a ", a)
a **= 3
print("nilai a **= 3, nilai a menjadi ", a)


# operasi bitwise
# OR
c = True
print("\n nilai c =", c)

c |= False
print("nilai c |=, nilai c menjadi", c)

c |= False
print("nilai c |= False, nilai c menjadi ", c)

c = False
print(" nilai c |= False, nilai c menjadi", c)

# AND
c = True
print("\n nilai c =", c)

c &= False
print("nilai c &=, nilai c menjadi", c)

c = True
print("nilai c &= False, nilai c menjadi ", c)

c &= True
print(" nilai c &= False, nilai c menjadi", c)


# XOR
c = True
print("\n nilai c =", c)

c ^= False
print("nilai c ^=, nilai c menjadi", c)

c = True
print("nilai c ^= False, nilai c menjadi ", c)

c ^= True
print(" nilai c ^= False, nilai c menjadi", c)


# geser geser
d = 0b0100
print(" nilai d =", format(d, '04b'))

d >>= 2
print("nilai d >>= 2, nilai d menjadi", format(d,'04b'))

d <<= 1
print("nilai d <<= 1, nilai d menjadi", format(d,'04b'))

