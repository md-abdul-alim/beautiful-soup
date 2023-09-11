import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.iplt20.com/auction"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

table = soup.find('table', class_ = "ih-td-tab auction-tbl")

headers = table.find_all('th')

columns = []

for i in headers:
	columns.append(i.text)

df = pd.DataFrame(columns=columns)

table_data = table.find_all('tr')[1:] #excluding header


for item in table_data:
	first_td = item.find_all('td')[0].find('div', class_ = 'ih-pt-ic').text.strip() #removing back slash
	data = item.find_all('td')[1:]

	row = [tr.text for tr in data]
	row.insert(0, first_td)

	lenght = len(df)
	df.loc[lenght] = row


df.to_csv("IPL_action.csv")
df.to_excel("IPL_action.xlsx")