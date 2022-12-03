import os,re,json,time,requests
# warna
K = ('\x1b[1;93m')
M = ('\x1b[1;91m')
H = ('\x1b[1;92m')
P= ('\x1b[1;97m')

class open:
    def __init__(self):
        os.system('clear')
        print(f"""
        {K}1.{H}open{P}
        {K}2.{M}exit{P}""")

        usna = input(f'{K}choose:{H}')
        if usna == '1' or usna == '01':
            session=requests.get('https://google.com')
        elif usna == '2' or usna == '02':
            exit('terima kasih bro dah mengunakan script ini')

if __name__=='__main__':
    os.system('git pull');open()