class Ojek():
	def __init__(self, nama, transmisi, daerah):
		self.nama = nama
		self.transmisi = transmisi
		self.daerah = daerah

	def cek_id_ojol(self):
		print('nama :', self.nama, '\nmotor :', self.transmisi, '\ndaerah :', self.daerah)


class Gojek(Ojek):
	
	def cek_id_ojol(self):
		print('cek aplikasi gojek')

ojek1 = Ojek('mario', 'manual', 'pontianak')
ojek2 = Gojek('revi', 'otomatis', 'bengkayang')

ojek1.cek_id_ojol()
ojek2.cek_id_ojol()