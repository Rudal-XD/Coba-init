import os,sys,json,requests

def __init__(self):
	print(f'1.open')
	self.pilih()
	
	def pilih(self):
		masuk = input('choose:')
		print()
		if masuk in ['']:
			print()
		elif masuk in ['1']:
			try:
				r=requests.get('https://google.com')
			except IOError:
				print('error')
		elif masuk in ['2']:
		 	print()
		 	exit()
		 	
if __name__=='__main__':
	os.system('git pull');Coba-init()
