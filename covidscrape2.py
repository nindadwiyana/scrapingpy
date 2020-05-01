# web scraping UTS
from bs4 import BeautifulSoup
import requests
import urllib.request as urllib2
import re
import csv


source = requests.get('https://www.kompas.com/covid-19').text

soup = BeautifulSoup(source, 'lxml')

# html_page = urllib2.urlopen("https://www.kompas.com/covid-19")
# soup = BeautifulSoup(html_page)

csv_file = open('covid19v2.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['link','artikel','provinsi', 'konfirmasi'])
    
for link in soup.find_all('a', class_='article__link', attrs={'href': re.compile("^https://")}):
    print (link.get('href'))

for div in soup.find_all('a','div', class_='article__list__title'):
    artikel = div.h3.a.text
    print(artikel)

    csv_writer.writerow([link, artikel])
    
for div in soup.find_all('div', class_='covid__row'):
    provinsi = div.find(class_='covid__prov').text
    print(provinsi)

    konfirmasi = div.find(class_='covid__total').span.text
    print(konfirmasi)

    print()

    csv_writer.writerow([link, provinsi, konfirmasi])

csv_file.close()