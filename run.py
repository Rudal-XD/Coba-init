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
{HIJAU}1.{PUTIH} Mendapatkan token EAAI
{HIJAU}2.{PUTIH} Dapatkan token EAAB
{HIJAU}3.{PUTIH} Cara menggunakan
{HIJAU}4.{PUTIH} Keluar {HIJAU}({MERAH}exit{HIJAU}){MERAH}
   """)
    masuk = input(f"{KUNING}?.{PUTIH} Choose :{HIJAU} ")
    if masuk == '1' or masuk == '01':

if __name__=='__main__':
  os.system('git pull');convert()
