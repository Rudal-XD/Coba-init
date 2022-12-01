import requests, json, time, re, os

# Warna
KUNING = ('\x1b[1;93m')
MERAH = ('\x1b[1;91m')
HIJAU = ('\x1b[1;92m')
PUTIH = ('\x1b[1;97m')
# Banner
banner = (f"""     {MERAH}({PUTIH}-Rudal-XD-{MERAH}){PUTIH}
{MERAH}╔═╗┌─┐┌┐┌┬  ┬┌─┐┬─┐┌┬┐
{MERAH}║  │ ││││└┐┌┘├┤ ├┬┘ │
{PUTIH}╚═╝└─┘┘└┘ └┘ └─┘┴└─ ┴
""")
# Convert Cookie Ke Token
class convert:

  def __init__(self):
    os.system('clear')
    print(f"""{banner}
{HIJAU}1.{PUTIH} Open 1
{HIJAU}2.{PUTIH} open 2
{HIJAU}3.{PUTIH} open 3
{HIJAU}4.{PUTIH} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}?.{PUTIH} Choose :{HIJAU} ")
    if masuk == '1' or masuk == '01':
    	try:
    		requests.get('https://google.com')
    	except IOError:
    		print('error')
    elif masuk == '2' or masum == '02':
    	exit()
    		
if __name__=='__main__':
	os.system('git pull');convert()
