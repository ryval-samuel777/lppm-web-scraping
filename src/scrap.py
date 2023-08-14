import requests
from bs4 import BeautifulSoup
import json
import os

# Fetch the webpage
url = 'https://lppm.unsrat.ac.id'
response = requests.get(url)
html = response.text

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find elements by tag 
articles = soup.find_all('article')

article_list = []

# Specify the absolute path to the data folder
destination_folder = '/home/error404/PROGRAMMING_LAB/python/web-scraping-lppm/data'


for article in articles:
    title = article.find('h2', class_='entry-title').a.text
    author = article.find('span', class_='entry-author').a.text
    date = article.find('span', class_='entry-date').time.text
    link = article.find('h2', class_='entry-title').a['href']

    # log the article information
    print("Title:", title)
    print("Author:", author)
    print("Date:", date)
    print("Link:", link)
    print("=" * 40)

    article_data = {
        'title': title,
        'author': author,
        'date': date,
        'link': link
    }
    article_list.append(article_data)

json_data = json.dumps(article_list, indent=4)

# Specify the JSON file path using the absolute path
json_filename = 'articles.json'
json_filepath = os.path.join(destination_folder, json_filename)

with open(json_filepath, 'w') as json_file:
    json_file.write(json_data)

print(f"JSON data has been written to '{json_filepath}'.")
