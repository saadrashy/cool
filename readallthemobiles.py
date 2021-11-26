import requests
import time	
from bs4 import BeautifulSoup
import subprocess
import datetime
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests
from deep_translator import (GoogleTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             DeepL,
                             QCRI,
                             single_detection,
                             batch_detection)
import requests



cred = credentials.Certificate('beautifulsoup-2e364-firebase-adminsdk-qsi94-302b0b8e26.json');
firebase_admin.initialize_app(cred, {'databaseURL': 'https://beautifulsoup-2e364-default-rtdb.firebaseio.com'})





mobiles ={ 'pagenumber': [1],
			'Mobilepage':[1],
			'Scanned': [0]}

mobilepageframe=pd.DataFrame(mobiles)



def switch_ip():

		#command = "sudo protonvpn c -r"
		#proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	while True:
		#	output = proc.stdout.readline()
		#	if proc.poll() is not None:
		#		break
		#	if output :
		#		print(output.strip())
		print("Change the IP")
		time.sleep(4)
		print("Change the IP Dear")
		time.sleep(4)
		resultxxx= requests.get("https://www.gsmarena.com")
		print("Requesting GSMArena")
		srcxxx =resultxxx.content #outerworld_page_number
		soupxxx = BeautifulSoup(srcxxx, 'lxml')
		print("I am checking")
		checkblock = soupxxx.select('title')[0].text.strip()
		if checkblock in ['GSMArena.com - mobile phone reviews, news, specifications and more...']:
			print("Everything is fine")
			break
		else:
			print("Not Yet, Another Chance")
    		


def first_page():

	global mobiles
	global mobilepageframe
	print(bcolors.OKBLUE + bcolors.BOLD +"https://www.gsmarena.com/samsung-phones-9.php" + bcolors.WARNING + "Changing the IP now, Tick Tick " + bcolors.ENDC)
	resultxxx= requests.get("https://www.gsmarena.com")
	srcxxx =resultxxx.content #outerworld_page_number
	soupxxx = BeautifulSoup(srcxxx, 'lxml')
	checkblock = soupxxx.select('title')[0].text.strip()
	if checkblock in ['GSMArena.com - mobile phone reviews, news, specifications and more...']:
		l=1
	else:
		switch_ip()
	result2= requests.get("https://www.gsmarena.com/samsung-phones-9.php")
	src2 =result2.content #outerworld_page_number
	soup2 = BeautifulSoup(src2, 'lxml')
	data2 = soup2.findAll('div',attrs={'class':'makers'})
	for div2 in data2:
		links2 = div2.findAll('a')
		for onelink in links2:
			mobiles = {'pagenumber':"https://www.gsmarena.com/samsung-phones-9.php", 'Mobilepage':onelink['href'],'Scanned':[0]}		
			mobilepageframe = mobilepageframe.append(mobiles,ignore_index=True)
			print(mobilepageframe)
		 

def next_page():

	global mobiles
	global mobilepageframe

	for x in range(2,17):
		print(bcolors.OKBLUE + bcolors.BOLD +"Fetching https://www.gsmarena.com/samsung-phones-f-9-0-p"+str(x)+".php " + bcolors.WARNING + "Changing the IP now, Tick Tick " + bcolors.ENDC)
		#time.sleep(10)
		#switch_ip()
		#time.sleep(10)

		resultxxx= requests.get("https://www.gsmarena.com")
		srcxxx =resultxxx.content #outerworld_page_number
		soupxxx = BeautifulSoup(srcxxx, 'lxml')
		checkblock = soupxxx.select('title')[0].text.strip()
		if checkblock in ['GSMArena.com - mobile phone reviews, news, specifications and more...']:
			l=1
		else:
			switch_ip()

		result2= requests.get("https://www.gsmarena.com/samsung-phones-f-9-0-p"+str(x)+".php")
		src2 =result2.content #outerworld_page_number
		soup2 = BeautifulSoup(src2, 'lxml')
		data2 = soup2.findAll('div',attrs={'class':'makers'})
		for div2 in data2:
			links2 = div2.findAll('a')
			for onelink in links2:
				#time.sleep(10)
				#switch_ip()
				#time.sleep(10)
				#data3 = soup3.findAll('div',attrs={'id':'specs-list'})
				#dfs = pd.read_html(src3)
				#print(dfs)
				#dfs2 = dfs.apply(translator.translate, src='en', dest='ar').apply(getattr, args=('text',))
				#table = soup3.table

				mobiles = {'pagenumber':"samsung-phones-f-9-0-p"+ str(x) +".php", 'Mobilepage':onelink['href'],'Scanned':[0]}		
				mobilepageframe = mobilepageframe.append(mobiles,ignore_index=True)
				print(mobilepageframe)
				mobilepageframe.to_pickle('mobile_pages.pkl')


				#table_rows = table.find_all('tr')
				#tables_body = tables.find_all('tr')
				#tables_row = tables_body.find_all('tr')
				#for row in tables_body:
				#		l.append(row)
				#		print(l)

				#for tr in table_rows:
					#td = tr.find_all('td')
					#row =[i.text for i in td]
					#print(row)
					#l.append(row)
					#print("\n Another Section")
					#translated = MyMemoryTranslator(source='auto', target='arabic').translate(row[0])
					#translated = GoogleTranslator(source='auto', target='ar').translate(row[1])  # output -> Weiter so, du bist großartig
					#print("\n")
					#print(translated)
				#df=pd.DataFrame(l,columns=["A","B"])
				#print(df)

			



#result = requests.get("https://www.gsmarena.com/")

#print(result.status_code)
#print(result.headers)
#time.sleep(10)
#src=result.content
#soup = BeautifulSoup(src, 'lxml')

#https://www.gsmarena.com/samsung-phones-9.php
#https://www.gsmarena.com/samsung-phones-f-9-0-p2.php
#https://www.gsmarena.com/samsung-phones-f-9-0-p3.php
#https://www.gsmarena.com/samsung-phones-f-9-0-p4.php
#https://www.gsmarena.com/samsung-phones-f-9-0-p16.php


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



#Downloading Pictures should be another session
#Spidering for information a different session. 
#Shouldnt be at same time. 



#check the last data, focus on pagenumber, use that data, to drop, the rowse from the list, and once again, start the crawling to add the page."


#letemreadthedata = pd.read_pickle('mobile_pages.pkl')
#sub_df = letemreadthedata.iloc[-1]
#thelastpagenumber = sub_df.iloc[-1]['pagenumber']
#remove = letemreadthedata.set_index("pagenumber")
#focused_the_database = rmemove.drop(thelastpagenumber, axis =0)
#focused_the_database.to_pickle('mobile_pages.pkl')



first_page()
next_page()



    		

#list = soup.find_all("li")
#print(list)

#links = list.find("a")

#print(links)