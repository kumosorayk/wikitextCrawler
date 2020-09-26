import requests
import os
from bs4 import BeautifulSoup

os.makedirs('./wikitext', exist_ok =True)
path = './wikitext'
os.chdir(path)

url = requests.get('http://wiki.example.com/Category:Example')
source_code = BeautifulSoup(url.text, 'html.parser')
pages = source_code.find_all('a', class_='category-page__member-link')

for info in pages:
    print(info.get('title'))
    print('http://wiki.example.com/' + info.get('href') + '?action=raw')
    wikipath = os.path.join(os.getcwd(), info.get('title').replace(':', ' ').replace('/', ' ') + '.wiki')
    file = open(wikipath, 'w+', encoding='utf-8')
    file.write(requests.get('http://wiki.example.com/' + info.get('href') + '?action=raw').text)
    file.close()
