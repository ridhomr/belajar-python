# program konversi celsius ke satuan lain
print("KONVERSI TEMPERATUR")

#================KONVERSI CELCIUS==================#
# konversi Celcius
celcius = float(input("Masukkan suhu dalam celcius :"))
print("suhu adalah : ", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah :", reamur, "Reamur")


# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")


# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, "Kelvin")

#================KONVERSI REAMUR====================#

# konversi Reamur
reamur = float(input("Masukkan value reamur :"))
print("value reamur adalah :", reamur, "Reamur")

# celcius
celcius = ((5/4) * reamur)
print("value celcius :", celcius, "celcius")

# fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("value fahrenheit :", fahrenheit, "Fahrenheit")

# kelvin
kelvin = 5/4 * reamur + 273
print("value kelvin :", kelvin, "Kelvin")

#===============KONVERSI FAHRENHEIT=================#

# konversi fahrenheit
fahrenheit = float(input("masukkan value fahrenheit :"))
print("value fahrenheit :", fahrenheit, "Fahrenheit")

# celcius
celcius = ((5/9) * fahrenheit) - 32
print("value celcius :", celcius, "Celcius")

# reamur
reamur = ((4/9) * fahrenheit) - 32
print("value reamur :", reamur, "Reamur")

#================KONVERSI KELVIN===================#

# konversi kelvin
kelvin = float(input("Masukkan value kelvin :"))
print("value kelvin :", kelvin, "Kelvin")

# celcius
celcius = kelvin - 273
print("value celcius :", celcius, "Celcius")

# reamur
reamur = ((4/5) * kelvin) - 273
print("value reamur :", reamur, "Reamur")
