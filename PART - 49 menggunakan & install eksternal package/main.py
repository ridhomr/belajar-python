# install python
# koneksi internet
# dependency


from PIL import Image

im = Image.open("tes.png")

print("format file :", im.format)
print("size file :", str(im.size))
print("mode file :", im.mode)


im.show()