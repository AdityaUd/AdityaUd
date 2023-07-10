# -*- coding: utf-8 -*-
"""
Created on Sun May  7 15:08:37 2023

@author: HP
"""

import requests
from bs4 import BeautifulSoup

GFG_req=requests.get('https://www.geeksforgeeks.org/')
soup_GFG = BeautifulSoup(GFG_req.content,'html.parser')

print(soup_GFG.prettify())

print(soup.get_text()) # () can have content tag

import requests
from bs4 import BeautifulSoup

url = "https://www.cnn.com" # change link
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

headlines = soup.find_all('h3', class_='cd__headline')
for headline in headlines:
    print(headline.get_text())

