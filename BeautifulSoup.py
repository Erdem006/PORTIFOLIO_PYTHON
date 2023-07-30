from bs4 import BeautifulSoup
import requests

link = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(link)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.prettify())