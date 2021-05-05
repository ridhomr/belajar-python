# ini adalah string

data = "ini adalah string"
print(data)
print(type(data))

# cara membuat string

'''
    1. dengan menggunakan single quote '...'
    2. kita bisa menggunakan duble quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "ini adalah menggunakan duble quote"
print(data)

# gabungan string duble quote dan single quote
print('"hallo apa kabar"')
print("'hallo apa kabar'")


print("ini adalah hari jum'at")

# 2. menggunakan tanda  \

# membuat tanda ' menjadi string

print('mari sholat jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\Ucup")


# tab
print("ucub\totong")

# backspace
print("ucup \botong")

# newline
print("baris pertama.\nbaris kedua.") # LF line feed (mac os, linux)
print("barus pertama. \rbaris kedua.") # CR carriage return (commodore, acorn lisp)
print("baris pertama. \r\nbaris kedua.") # CSLF line feed carriage return (dipakai oleh windows)

# 3. string literal atau raw

# hati - hati
print('C:\\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline untuk literal string
print("""
nama : Ucup
kelas : 2 SD
""")

# multiline literal string dan raw

print(r"""
nama : ucup
kelas : 2 SD
website : ucup.com/newweb
""")
