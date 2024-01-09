from bs4 import BeautifulSoup
import requests

class ArxivFeed:
    def __init__(self):
        url=requests.get('http://export.arxiv.org/rss/astro-ph.CO/new')
        self.soup=BeautifulSoup(url.content,'xml')
        self.items=self.soup.find_all('item')
    def get_items(self):
        return self.items

list = []

if __name__=='__main__':
    items=ArxivFeed().items
    for item in items:
        list.append([item.title.text , item.description.text]) 
        print(item.description.text)
        break

