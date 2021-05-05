class rumah():

	def __init__(self, gitar, hp, laptop):
		self.gitar = gitar
		self.hp = hp
		self.laptop = laptop

	def gitar_yh(self, gitar):
		print(self.gitar, "adalah merk", gitar)

	def hp_yh(self, hp):
		print(self.hp, "adalah hp dari", hp)

	def laptop_yh(self, laptop):
		print(self.laptop, "laptop dari", laptop)

rumah_ridho = rumah("yamaha", "android", "mac")
print(rumah_ridho.gitar)
print(rumah_ridho.hp)
print(rumah_ridho.laptop)


rumah_ridho.gitar_yh("YZX")
rumah_ridho.hp_yh("cina")
rumah_ridho.laptop_yh("amerika")
