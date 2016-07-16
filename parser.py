#网页解析器
from bs4 import BeautifulSoup
import re
class Parser():
    def __init__(self):
        pass
    def parse(self,con):
        bs=BeautifulSoup(con,'html.parser',from_encoding='utf8')
        title=bs.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1').get_text()
        text=bs.find('div',class_='lemma-summary').get_text()
        allurls=bs.find_all('a',href=re.compile(r'/view/\d+\.htm'))
        urls=[]
        for url in allurls:
            urls.append(url['href'])
        return title,text,urls
        
