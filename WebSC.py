from bs4 import BeautifulSoup
import requests

link = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(link)

soup = BeautifulSoup(page.text, 'html.parser')

soup.find('div')
##print(soup.find('div'))

soup.find_all('div')
##print(soup.find_all('div'))

soup.find_all('div', class_ = 'col-md-12')
##print(soup.find_all('div', class_ = 'col-md-12'))

soup.find('p', class_ = 'lead').text.strip()