# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 20:22:52 2020

@author: 150566
"""
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 
import requests

#FLipkart
product = "boat earphones"#input('Enter the product to compare: ')
baseurl = "https://www.flipkart.com"
url = "https://www.flipkart.com/search?q=" + product
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
product_links = []
ratings = []
specifications1 = []
name1 = []
price1 = []

for i in range(1, 8): #going through all the pages from 1 - 8
    pg = url + "&page=" + str(i) #changing url according to page number
    page = requests.get(pg)
    soup = BeautifulSoup(page.content, 'lxml') 
    title = soup.find_all('div', class_='E2-pcE _1q8tSL')
    print(title)
    for item in title:
        for link in item.find_all('a', href = True):
            product_links.append(baseurl + link['href'])
            print(product_links)
for link in product_links:
        pages = requests.get(link)
        soup = BeautifulSoup(pages.content, 'lxml')
        for names in soup.find_all('div', class_ = '_1i0wk8'):
            if names.get_text():
                rating = names.get_text()
            else: rating = "No ratings yet"
            ratings.append(rating)
        for specifications in soup.find_all('div', class_ = '_2RngUh'):
            specification = specifications.text
            specifications1.append(specification)

        for name in soup.find_all('h1', class_ = '_9E25nV'):
            name1.append(name)
        for price in soup.find_all('div', class_ = '_1uv9Cb'):
            prices = price.text
            price1.append(prices)
print(price1)

            
###Amazon


