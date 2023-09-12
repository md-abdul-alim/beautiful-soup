import requests
import pandas as pd
from bs4 import BeautifulSoup

urls = []
names = []
prices = []
descriptions = []
ratings = []

counter = 1
# for i in range(1, 45):
while counter > 0:
	url = "https://www.rokomari.com/book/category/3402/boimela-2023-novel?page=" + str(counter)
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text, 'lxml')
	 
	items = soup.find_all('div', class_='_2kHMtA')
	if len(items) > 0:
		for item in items:
			url = 'https://www.flipkart.com' + item.find('a', class_='_1fQZEK')['href']
			urls.append(url)

			name = item.find('div', class_='_4rR01T').text
			names.append(name)

			if item.find('div', class_='_30jeq3 _1_WHN1'):
				price = item.find('div', class_='_30jeq3 _1_WHN1').text
				prices.append(price)
			else:
				prices.append('None')

			description = item.find_all('li', class_='rgWa7D')
			concat_description = ''
			for i in description:
				concat_description += ',' + i.text
			descriptions.append(concat_description)

			
			if item.find('div', class_='gUuXy-'):
				rating = item.find('div', class_='gUuXy-').span.div.text
				ratings.append(rating)
			else:
				ratings.append('None')
	else:
		break
	counter += 1

print(len(urls), len(names), len(prices), len(descriptions), len(ratings))
df = pd.DataFrame({'Product Name': names, 'Price': prices,
				 'Rating': ratings, 'Description': descriptions, 'URL': urls })

print(df)
# df.to_csv("prducts_details.csv")
# df.to_excel("prducts_details.xlsx")