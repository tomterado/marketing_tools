# import libraries
# -*- coding: utf-8 -*-
##import re
##import urllib.request
##import urllib

import urllib2
from bs4 import BeautifulSoup

data = ['https://icobench.com/ico/comsa','https://icobench.com/ico/blockmason','https://icobench.com/ico/bitboost']
for pg in data:
 	page = urllib2.urlopen(pg)
 	soup = BeautifulSoup(page, 'html.parser')
 	for link in soup.find_all('a'):
 		whitepaper_link = link.get('href')
 		if whitepaper_link.endswith('pdf'):
 			print whitepaper_link

 	# for start_date in start_box:
 	# 	#ico_start = start_box.find("ICO start")
 	# 	start_date = [b.string for b in start_box.findAll('b')]
 	# 	#if start_box1.endswith('2017'):
 	# 	#start_box = ico_start
 	# 	print start_date

	# if price is None:
	# 	continue
	# else:
	# 	print price

	# prtyp = soup.find("dd", attrs={"class":"is_type g"}).text.strip() 
	# if soup.find("dd", attrs={"class":"is_type g"}) else "no type"

	#     if prtyp is None:
 #       prtyp = "no type"
 #    else:
 #       # whgtyp.text.strip() # I don't know what it does
 #       print("prtype:", prtype)


	# try:
	# 	print price
	# except None:
	# 	print('Rating error')


 	# for price in price_box:
 	# 	if price_box.text is not None:
 	# 		print price

 # 	price = price_box.text
	# if price is not None:

	# 	print price


	# for rate in soup.find_all('div',{"class":"rating"}):
 #    	if rate.img is not None:
 #        	print (rate.img['alt'])
 	# m = None
 	# if (price == m):
 	# 	continue
 	# print price