import requests
import pandas as pd
from bs4 import BeautifulSoup


url = "https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"

html_text = requests.get(url).text

soup = BeautifulSoup(html_text, 'lxml')

table = soup.find('table', class_ = "ih-td-tab auction-tbl")