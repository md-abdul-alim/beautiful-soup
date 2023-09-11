import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

urls = []
names = []
prices = []
descriptions = []
ratings = []
 
items = soup.find_all('div', class_='_2kHMtA')

for item in items:
	url = 'https://www.flipkart.com' + soup.find('a', class_='_1fQZEK').text

	print(url)
	urls.append(url)
	name = soup.find('div', class_='_4rR01T').text
	names.append(name)
	price = soup.find('div', class_='_30jeq3 _1_WHN1').text
	prices.append(price)

	description = soup.find_all('li', class_='rgWa7D')
	concat_description = ''
	for i in description:
		concat_description += ',' + i.text
	descriptions.append(concat_description)

	rating = soup.find('div', class_='gUuXy-').span.div.text
	print(rating)
	ratings.append(rating)

print(len(url), len(names), len(prices), len(descriptions), len(ratings))
# df = pd.DataFrame({'Product Name': names, 'URL': url, 'Price': prices,
# 				 'Rating': ratings, 'Description': descriptions })

# print(df)
# df.to_csv("prducts_details.csv")
# df.to_excel("prducts_details.xlsx")