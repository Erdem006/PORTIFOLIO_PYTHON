from bs4 import BeautifulSoup
import requests

link = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(link)

soup = BeautifulSoup(page.text, 'html.parser')
##print(soup)

soup.find_all('table')
##print(soup.find_all('table'))

soup.find('table', class_ = 'wikitable sortable')
##print(soup.find('table', class_ = 'wikitable sortable'))

table =  soup.find_all('table')[1]
##print(table)

columnTitle = table.find_all('th')
##print(columnTitle)

tableTitle = [title.text.strip() for title in columnTitle]
##print(tableTitle)

import pandas as pd
df = pd.DataFrame(columns = tableTitle)

column_data = table.find_all('tr')

for row in column_data[1:]:
    row_data = row.find_all('td')
    induvisual_row_data = [data.text.strip() for data in row_data]
    ##print(induvisual_row_data),
    length = len(df)
    df.loc[length] = induvisual_row_data

df.to_csv(r'C:\Users\bowie\OneDrive\Masaüstü\Companies.csv', index = false)