import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://ticker.finology.in/"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

table = soup.find('table', class_ = "table table-sm table-hover screenertable")

table_headers = table.find_all('th')
columns = []


for i in table_headers:
	columns.append(i.text)

df = pd.DataFrame(columns=columns)

table_data = table.find_all('tr')[1:] #excluding header


for item in table_data:
	data = item.find_all('td')
	row = [tr.text for tr in data]
	lenght = len(df)
	df.loc[lenght] = row


// df.to_csv("table_data.csv")