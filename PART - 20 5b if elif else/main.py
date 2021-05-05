# penggunaan if
nilai = 50

if nilai == 75: # equel eksplisit
    print("nilai anda:", nilai)

if nilai is  50: # equal
    print("nilai anda:", nilai)

if nilai is not 60: # not equal
    print("nilai anda bukan: 60")


print(10*"=")
nilai = 50

# penggunaan elif
if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("nilai anda tidak lulus mata kuliah ini")

print(10*"+")
