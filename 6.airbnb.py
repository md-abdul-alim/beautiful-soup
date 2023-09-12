import requests
import pandas as pd
from bs4 import BeautifulSoup

name_list = []
description_list = []
price_list = []
rating_list = []

url = "https://www.airbnb.com/s/New-Delhi--India/homes?adults=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

for i in range(1, 14):
	next_url = soup.find('a', class_='c1ytbx3a').get('href')
	cnp = 'https://www.airbnb.com' + next_url

	html_text = requests.get(cnp).text
	soup = BeautifulSoup(html_text, 'lxml')

	# Name List
	names = soup.find_all('div', class_ = 't1jojoys')
	for name in names:
		name_list.append(name.text)

	# Description List
	descriptions = soup.find_all('span', class_ = 't6mzqp7')
	for description in descriptions:
		description_list.append(description.text)

	# Price List
	if soup.find_all('span', class_ = '_tyxjp1'):
		prices = soup.find_all('span', class_ = '_tyxjp1')
		for price in prices:
			price_list.append(price.text)
	if soup.find_all('span', class_ = '_1y74zjx'):
		prices = soup.find_all('span', class_ = '_1y74zjx')
		for price in prices:
			price_list.append(price.text)

	# Rating List
	if soup.find_all('span', class_ = 'r1dxllyb'):
		ratings = soup.find_all('span', class_ = 'r1dxllyb')
		for rating in ratings:
			rating_list.append(rating.text)
	else:
		print("IN")
		rating_list.append('None')

print(len(name_list), len(description_list), len(price_list), len(rating_list))

df = pd.DataFrame({'Name': name_list, 'Prices/night': price_list, 'Rating': rating_list, 'Description': description_list})

print(df)
# df.to_csv("prducts_details.csv")
# df.to_excel("prducts_details.xlsx")