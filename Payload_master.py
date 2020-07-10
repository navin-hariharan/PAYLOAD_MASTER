#!/usr/bin/python3 env
import os
import random
import time
import Payloads.pld_types as plds
from sys import platform
rows, columns = os.popen('stty size', 'r').read().split()
Colms =  int ((int (columns)-37) / 2)-2
c = " " * Colms

colors = ["\033[1;31m","\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
fore = random.choice (colors)
fore1 = "\033[1;36m"
fore2 = "\033[1;35m"
os.system ("clear")
blue = "\033[1;34m"
cyan = "\033[1;36m"




def banner ():
    os.system ("clear")
    print (" \n ")
    print (fore+"     o        o ")
    print (fore+"      o      o")
    print (fore+"       0 ■■ 0")
    print (fore+"       ■■■■■■ ")
    print (fore+"      ■■"+fore1+"▣"+fore+"■■"+fore1+"▣"+fore+"■■")
    print (fore+"     ■■■■■■■■■■")
    print (fore+"  __ __________ __")
    print (fore+"  ■■ ■■■■■■■■■■ ■■")
    print (fore+"  ■■ ■■■■■■■■■■ ■■")
    print (fore+"  ■■ ■■■■■■■■■■ ■■")
    print (fore+"     ■■■■■■■■■■ ")
    print (fore+"       ■■  ■■ ")
    print (fore+"       ■■  ■■")
    print ("\033[1;36mCooded By \033[1;34m :----->>   \033[1;31m Navin Hariharan   \033[1;34m")
    print ("\033[1;36mInsagram  \033[1;34m :----->>   \033[1;31m navin_hariharan \033[1;34m")
    print ("\033[1;36mGitHub    \033[1;34m :----->>   \033[1;31m navin-hariharan  \033[1;34m\n\n")





def Check_requirments ():
	if platform == "linux" or platform == "linux2":
	    if os.path.exists ("navin_playload") == False :
		    os.system ("mkdir navin_playload")
	else:
	    if os.path.exists ("/sdcard/navin_playload") == False :
		    os.system ("mkdir /sdcard/navin_playload")

	    if os.path.exists ('/data/data/com.termux/files/usr/bin/msfconsole') == True :
		    print ("")
	    else:
		    print("\033[1;31mMetasploit Not Installed 😢")
		    print("\033[1;36mHit Enter To Install..")
		    os.system('read ch')
		    os.system("pkg install unstable-repo;pkg install metasploit")
		    os.system('clear')
		    banner ()
def chose_opt ():
	print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+" Choose Your Payload\n")
	time.sleep (0.5)
	pld_list = ["Android" ,"Windows", "Linux", "Mac","Python","Bash", "Perl","Exit"]
	for pld in pld_list:
		time.sleep (0.1)
		print (cyan+"	["+blue,pld_list.index (pld)+1,cyan+"]   "+pld)
	print(" \n ")
	pld_type = int (input (" \033[1;34mNavin_payload\033[1;31m/~  \033[1;36m"))
	if pld_type > 8:
		try:
			raise ValueError
		except ValueError:
			time.sleep(3)
			exit (0)

	else:
		pld_to_gen = ["plds.Android ()", "plds.Windows ()", "plds.Linux()", "plds.Mac ()", "plds.Python ()", "plds.Bash ()", "plds.Perl ()", "exite ()"]
		exec (pld_to_gen[pld_type - 1])



def exite ():
	time.sleep (1.2)
	banner()
	print ("\033[1;34mNavin_payload\033[1;31m/~"+cyan+"  BY BY SEE YOU SOON.\n\n")
	exit (0)


def main ():
	os.system("rm -rf meterpreter_droid.rc metasploit_install.rc __pycache__ navin_playload/* Payloads/__pycache__;killall -2 ngrok > /dev/null")
	banner ()
	Check_requirments ()
	time.sleep (1.5)
	chose_opt ()


if __name__ == "__main__":
	try:
		main ()
	except KeyboardInterrupt:
		exite ()
	except ValueError:
		time.sleep()
		exit (0)
	except EOFError:
		exite ()
