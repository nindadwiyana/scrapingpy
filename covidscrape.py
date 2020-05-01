from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.okezone.com/covid-19').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('covid19.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['terkonfirmasi', 'sembuh'])

for div in soup.find_all('div', class_='data-fist'):
    terkonfirmasi = div.find(class_='col-12 nmb').text
    print(terkonfirmasi)

    sembuh = div.find(class_='col-12 jdl').text
    print(sembuh)


    print()

    csv_writer.writerow([terkonfirmasi, sembuh])

csv_file.close()