import requests
import json
import pandas as pd

url = "https://www.prothomalo.com/route-data.json?path=%2Fsports%2Fcricket"

response = requests.get(url)

title, news_detail_url, image_url, short_description = [], [], [], []

if response.status_code == 200:
    # Parse the JSON data
    data = response.json()

    items = data.get('data')['collection']['items']

    for item in items:
        # print('Title: ', item['story']['headline'])
        title.append(item['story']['headline'])
        # print('Details: ', item['story']['url'])
        news_detail_url.append(item['story']['url'])
        # print('Image URL: ', "https://images.prothomalo.com/" + item['story']['hero-image-s3-key'])
        image_url.append("https://images.prothomalo.com/" + item['story']['hero-image-s3-key'])
        # print('Short description: ', item['story']['metadata']['excerpt'])
        short_description.append(item['story']['metadata']['excerpt'])
        # print("---------------------------------")
else:
    print("Failed to retrieve data. Status code:", response.status_code)


df = pd.DataFrame({'Title': title, 'Detail URL': news_detail_url,
                 'Image URL': image_url, 'Description': short_description})

print(df)
# df.to_csv("prducts_details.csv")
df.to_excel("p.alo.cricket.xlsx")