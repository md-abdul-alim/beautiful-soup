import requests
import pandas as pd
from bs4 import BeautifulSoup

names, authors, prices, discount_prices, reviews, urls = [], [], [], [], [], []

counter = 1

while counter > 0 :
	url = "https://www.rokomari.com/book/category/3402/boimela-2023-novel?page=" + str(counter)
	html_text = requests.get(url).text
	soup = BeautifulSoup(html_text, 'lxml')
	 
	items = soup.find_all('div', class_='book-list-wrapper')

	if len(items) > 0:
		for item in items:
			url = 'https://www.rokomari.com' + soup.find('div', class_ = 'book-list-wrapper').a['href']
			urls.append(url)

			name = item.find('h4', class_='book-title').text
			names.append(name)

			author = item.find('p', class_='book-author').text
			authors.append(author)

			if item.find('span', class_='text-secondary'):
				review = item.find('span', class_='text-secondary')
				reviews.append(review.text.split('(')[1].split(')')[0])
			else:
				reviews.append('')

			if item.find('p', class_='book-price'):
				price = item.find('p', class_='book-price').text
				if len(price.split(" ")) == 6:
					prices.append(price.split(" ")[2]  + ' TK')
					discount_prices.append(price.split(" ")[4]  + ' TK')
				elif len(price.split(" ")) == 4:
					prices.append(price.split(" ")[2]  + ' TK')
					discount_prices.append('')
			else:
				prices.append('')
	else:
		break
	counter += 1

print(len(urls), len(names), len(authors), len(prices), len(reviews))
df = pd.DataFrame({'Book Name': names, 'Author': authors,
				 'Price': prices, 'Discount price': discount_prices,
				 'Review': reviews, 'URL': urls })

# print(df)
# df.to_csv("rokomari.csv")
df.to_excel("rokomari.xlsx")