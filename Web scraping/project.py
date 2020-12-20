from typing import re

import requests
from bs4 import BeautifulSoup

url = 'https://main.sci.gov.in/case-status#'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
print(soup.get_text())


for link in soup.find_all('a', attrs='href'):
        print(link)
        type(link)

file = open("parsed_data.txt", "w")
for link in soup.find_all('a', attrs='href'):
    soup_link = str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close()
