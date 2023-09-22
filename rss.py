from bs4 import BeautifulSoup
import requests

class ArxivFeed:
    def __init__(self):
        url=requests.get('http://export.arxiv.org/rss/astro-ph.CO/recent')
        self.soup=BeautifulSoup(url.content,'xml')
        self.items=self.soup.find_all('item')
    def get_items(self):
        return self.items

if __name__=='__main__':
    items=ArxivFeed().items
    for item in items:
        print('arxiv:',item.link.text.split('/')[-1])
        print(item.title.text)
        print('\n')
        print(item.description.text)
        print('\n\n\n')
        print('---'*10)
