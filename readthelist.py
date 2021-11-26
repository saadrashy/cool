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


mobilepageframe = pd.read_pickle('mobile_pages.pkl')
print(mobilepageframe)

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