# latihan komparasi dan logika

# soal 1
# -------0+++++++5-------8+++++++11--------

# memeriksa nilai lebih dari 0
# -------0+++++++

inputUser = float(input("masukkan angka lebih dari nol :"))
nolLebihDari = (inputUser > 0)
print("lebih besar dari 0 =", nolLebihDari)


# +++++++5------
kurangdari5 = (inputUser < 5)
print("kurang dari 5 =", kurangdari5)


# -------8+++++++
lebihDari8 = (inputUser > 8)
print("lebih dari 8 =", lebihDari8)


# +++++++11------
kurangDari11 = (inputUser < 11)
print("kurang dari 11 =", kurangDari11)



# soal 2
# +++++++0-------5+++++++8-------11++++++++

# +++++++0-------
inputUser = float(input("masukkan angka kurang dari 0 :"))
krngDari0 = (inputUser < 0)
print("kurang dari 0 =", krngDari0)

# -------5+++++++
lbhDari5 = (inputUser > 5)
print("lebih dari 5 =", lbhDari5)

# +++++++8-------
krgDari8 = (inputUser < 8)
print("kurang dari 8 =", krgDari8)

# -------11++++++
lbhDari11 = (inputUser > 11)
print("lebih dari 11 =", lbhDari11)