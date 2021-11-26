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

data2 = {'Mobile':[1,1],
'Category':[1,1],
'Type':[1,1],
'Value':[1,1]
}
df1 = pd.DataFrame(data2)

def switch_ip():
    command = "sudo protonvpn c -r"
    proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
    	output = proc.stdout.readline()
    	if proc.poll() is not None:
    		break
    	if output :
    		#print(output.strip())
    		l=1



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

for x in range(10):
	if x >= 2 :
		print(bcolors.OKBLUE + bcolors.BOLD +"Fetching https://www.gsmarena.com/samsung-phones-f-9-0-p"+str(x)+".php " + bcolors.WARNING + "Changing the IP now, Tick Tick " + bcolors.ENDC)
		#time.sleep(10)
		#switch_ip()
		#time.sleep(10)
		result2= requests.get("https://www.gsmarena.com/samsung-phones-f-9-0-p"+str(x)+".php")
		src2 =result2.content #outerworld_page_number
		soup2 = BeautifulSoup(src2, 'lxml')
		data2 = soup2.findAll('div',attrs={'class':'makers'})
		for div2 in data2:
			links2 = div2.findAll('a')
			for onelink in links2:
				print( onelink['href']) #single_model_page
				#time.sleep(10)
				#switch_ip()
				#time.sleep(10)
				print("IP switched, Fetching", "https://www.gsmarena.com/"+onelink['href'])
				result3= requests.get("https://www.gsmarena.com/"+onelink['href'])
				src3 =result3.content #outerworld_page_number
				soup3 = BeautifulSoup(src3, 'lxml')
				#data3 = soup3.findAll('div',attrs={'id':'specs-list'})
				#dfs = pd.read_html(src3)
				#print(dfs)
				#dfs2 = dfs.apply(translator.translate, src='en', dest='ar').apply(getattr, args=('text',))
				#table = soup3.table
				tables = soup3.find_all('table')
				l =[]
				ll=[]
				#for table in tables:
				#	ths = table.find_all('th')
				#	for th in ths:
				#		#row =[i.text for i in th]
				#		print(th.text)

				df = pd.DataFrame(columns=['Attributes','values'])
				for table in tables: #for a table in tables.
					trs = table.find_all('tr') #Tfor a table in tables.find all the trs.
					for tds in trs:				#In each Trs, you are going into one tr
						th =tds.find_all('th')
						for y in th:
							category = y.text
							#print(bcolors.OKGREEN + bcolors.BOLD +rowth)
						td =tds.find_all('td')	#in each tr, you find many tds
						for i in td:
							try:
								if i['class'][0] == 'ttl':
									if i.text in ['\xa0']:
								#if row[0] in ['2G bands']:
								#	lasttext="2G" +" اقات "
								#df = df.append({"Attributes": lasttext, "values":row[1]}, ignore_index=True)
								#	print(bcolors.OKGREEN + bcolors.BOLD + lasttext)
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
								#translated2= MyMemoryTranslator(source='auto', target='arabic').translate(row[1])
								#print(bcolors.OKBLUE + translated2)
								#if row[0] in ['3G bands']:
								#	lasttext="3G" +" اقات "
								#df = df.append({"Attributes": lasttext,"values":row[1]}, ignore_index=True)
								#	print(bcolors.OKGREEN + bcolors.BOLD + lasttext)
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
								#translated2= MyMemoryTranslator(source='auto', target='arabic').translate(row[1])
								#print(bcolors.OKBLUE + translated2)
								#if row[0] in ['4G bands']:
								#	lasttext="4G" +" اقات "
								#df = df.append({"Attributes": lasttext,"values":row[1]}, ignore_index=True)
								#	print(bcolors.OKGREEN + bcolors.BOLD + lasttext)
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
								#translated2= MyMemoryTranslator(source='auto', target='arabic').translate(row[1])
								#print(bcolors.OKBLUE + translated2)
								#if row[0] in ['5G bands']:
								#	lasttext="5G" +" اقات "
								#df = df.append({"Attributes": lasttext,"values":row[1]}, ignore_index=True)
								#	print(bcolors.OKGREEN + bcolors.BOLD + lasttext)
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
								#translated2= MyMemoryTranslator(source='auto', target='arabic').translate(row[1])
								#print(bcolors.OKBLUE + translated2)
								
								#df = df.append({"Attributes": lasttext,"values":row[1]}, ignore_index=True)
										print("Null")
									else:
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
							#translated = MyMemoryTranslator(source='auto', target='arabic').translate(row[0])
							#lasttext = translated
										vtype = i.text
								if i['class'][0] == 'nfo':
									if i.text in ['\xa0']:
										print("Null")
									else:
										vvalue = i.text
										data2 = {
											'Mobile':onelink['href'],
    										'Category':[category],
    										'Type':[vtype],
    										'Value':[vvalue],
												}
										df1=df1.append(data2,ignore_index=True)

							except KeyError:
								print("KeyError")
								#time.sleep(10)
								#switch_ip()
								#time.sleep(10)
							#translated2= MyMemoryTranslator(source='auto', target='arabic').translate(row[1])
							#	print(bcolors.OKBLUE + i.text)
							
							#df = df.append({"Attributes": lasttext,"values":translated2}, ignore_index=True)
				print(df1)
				df1.to_pickle('mobile_data.pkl')		

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

			





    		

#list = soup.find_all("li")
#print(list)

#links = list.find("a")

#print(links)