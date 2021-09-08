# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:11:51 2020

@author: Chitra Bhat
"""
import csv

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import requests
product = 'laptop' 

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
baseurl1 = "https://www.amazon.in"
url1 = "https://www.amazon.in/s?k=" + product
product_links1 = []
ratings1 = []
specifications2 = []
name2 = []
price2 = []


for i in range(1,8):
    burl = url1 + "&page=" + str(i)
    
    page1 = requests.get(burl, headers = headers)
    soup = BeautifulSoup(page1.content, 'lxml')
    product = soup.find_all('a', {'class' : 'a-link-normal a-text-normal'})
    for link in product:
        links = baseurl1 + link.get('href')
        product_links1.append(links)
for link in product_links1:
    pages1 = requests.get(link, headers = headers)
    soup = BeautifulSoup(pages1.content, 'lxml')
    for names in soup.find_all('span' , class_ = 'a-size-large product-title-word-break'):
        nam = names.text
        name2.append(nam)
    for prices in soup.find_all('span', class_ = 'a-size-medium a-color-price priceBlockBuyingPriceString'):
        pri = (prices.text)
        price2.append(pri)
    for specifications in soup.find_all('div', class_ = 'a-section a-spacing-medium a-spacing-top-small'):
        m = specifications.text
        m.replace('\n', '')
        specifications2.append(m)
        
print(specifications) 

        specifications2.append()
    print([item.get_text(strip=True) for item in soup.select("span.a-icon-alt")])
