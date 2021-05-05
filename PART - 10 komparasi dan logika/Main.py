# latihan komparasi dan logika

# membuat gabungan dari area rentang dari sebuah angka

# ++++++++3------------10+++++++++
inputUser = float(input("Masukkan angka\n yang bernilai kurang dari \n 3 atau lebih besar dari 10:"))

# ++++++++3------------
# memeriksa angka kurang dari 3

isKurangDari = (inputUser < 3)
print("kurang dari 3 =", isKurangDari)



#+++++++++10-----------

# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("lebih dari 10 =", isLebihDari)


isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan :", isCorrect)


# ---------3+++++++++++10------------

# KASUS IRISAN
print("\n", 10*"=", "\n")
inputUser = float(input("Masukkan angka\n yang bernilai lebih dari \n 3 dan kurang dari 10:"))

# --------3+++++++++++++
# lebih dari 3
isLebihDari = inputUser > 3
print("lebih dari 3 =",isLebihDari)


# ++++++++10------------
# kurang dari 10

isKurangDari = inputUser < 10
print("kurang dari 10 =", isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan :", isCorrect)