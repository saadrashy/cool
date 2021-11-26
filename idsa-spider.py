import requests
import time	
from bs4 import BeautifulSoup
import subprocess
import datetime


def switch_ip():
    command = "sudo protonvpn c -r"
    proc = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    



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
		time.sleep(5)
		switch_ip()
		result2= requests.get("https://www.gsmarena.com/samsung-phones-f-9-0-p"+str(x)+".php")
		src2 =result2.content #outerworld_page_number
		soup2 = BeautifulSoup(src2, 'lxml')
		data2 = soup2.findAll('div',attrs={'class':'makers'})
		for div2 in data2:
			links2 = div2.findAll('a')
			for onelink in links2:
				print( onelink['href']) #single_model_page
				time.sleep(5)
				print(bcolors.OKBLUE + bcolors.BOLD + "Rotating the IP now, Tick Tick " + bcolors.ENDC)
				switch_ip()




def samsung():
	data = soup.findAll('div',attrs={'class':'brandmenu-v2'});
	count = 1
	for div in data:
	    links = div.findAll('a')
    	for a in links:
    		result2 = requests.get("http://www.gsmarena.com/" + a['href'])
    		time.sleep(10)
    		src2 =result2.content
    		soup2 = BeautifulSoup(src2, 'lxml')
    		data2 = soup2.findAll('div',attrs={'class':'makers'})
    		for div2 in data2:
    			links2 = div2.findAll('a')
    			for a2 in links2:
    				time.sleep(10)
    				result3 = requests.get("http://www.gsmarena.com/" + a2['href'])
    				src3 =result3.content
    				soup3 = BeautifulSoup(src3, 'lxml')
    				data3 = soup3.findAll('div',attrs={'class':'specs-photo-main'})
    				for div3 in data3:
    					print(count)
    					count = count + 1
    					links3 = div3.findAll('a')
    					for a3 in links3:
    						print( a3['href'])

    		

#list = soup.find_all("li")
#print(list)

#links = list.find("a")

#print(links)