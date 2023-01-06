import pandas as pd     #install all in settings below
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# create a driver instance (need to download and replace with your folder link)
s=Service("C:\\Users\\jessi\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=s)

# open the url
driver.get('https://westportlibrary.libguides.com/c.php?g=431564&p=8816383')

# get the html page
content = driver.page_source
html_page = driver.page_source

# create a soup object
soup = BeautifulSoup(html_page,'html.parser')

# find spans with class attribute name and s-lg-book-title value
title_elements = soup.find_all('span', class_ = 's-lg-book-title')

# find spans with class attribute name and s-lg-book-author value
author_elements = soup.find_all('span', class_ = 's-lg-book-author')

# create two empty lists
title_list = []
author_list = []

# iterate over the elements and get text
for title in title_elements:
    title_list.append(title.text)

for author in author_elements:
    author_list.append(author.text)

# create a dataframe
df = pd.DataFrame({'title':title_list, 'author':author_list})

# export to csv file
df.to_csv('bestsellers.csv', index=False, encoding='utf-8')
print(title_list)

# close the driver
driver.close()