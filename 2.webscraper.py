import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')
# header_attrs = header_tag.attrs
# header_key = header_attrs['class']

## Lession 1
items = soup.find_all('div', class_ = "col-sm-4 col-lg-4 col-md-4")

names = []
item_urls = []
prices = []
descriptions = []
reviews = []

for index, item in enumerate(items):
	name = item.find('a', class_ = 'title').text
	item_url = 'https://webscraper.io' + item.div.div.a['href']
	price = item.find('h4', class_ = 'pull-right price').text
	description = item.find('p', class_ = 'description').text
	review = item.find('div', class_ = 'ratings').p.text.split(' ')[0]

	names.append(name)
	item_urls.append(item_url)
	prices.append(price)
	descriptions.append(description)
	reviews.append(review)
	# print(name)
	# print('https://webscraper.io' + item_url)
	# print(price)
	# print(description)
	# print(review)
	# print("__________________________________________")

df = pd.DataFrame({'Product Name': names, 'URL': item_urls,
					'Price': prices, 'Review': reviews, 'Description': descriptions })

# df.to_csv("prducts_details.csv")
# df.to_excel("prducts_details.xlsx")

# Lession 2 - Navbar access
nav = soup.find('li', class_ = 'active')
category = nav.find('a', class_ = 'category-link').text
print(category)
subcategory = nav.find('a', class_ = 'subcategory-link active').text
print(subcategory)

## Lession 3 - Use of Regex
regex_data = soup.find_all(string = re.compile("Galaxy"))
# print(regex_data)

## Lession 3