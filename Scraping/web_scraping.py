import csv
import datetime
import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    
    def scrape(self):
        r = requests.get(self.site)
        content = r.content
        soup = BeautifulSoup(content, 'html.parser')

        now = datetime.datetime.now()
        print(now.strftime('%Y年%m月%d日%H時%M分%S秒'))

        fav = 400
        
        with open("test.csv", "a", newline='') as f:
            w = csv.writer(f)
            w.writerow(["取得時間：" + now.strftime('%Y年%m月%d日%H時%M分%S秒')])
            for div in soup.select("div.entrylist-contents-main"):
                title = div.h3
                url = div.a
                user = div.span
                user_num = user.getText().split(" ")
            
                if int(user_num[0]) >= fav:
                    print(title.getText())
                    print(url.get('href'))
                    print(user.getText())
                    w.writerow([title.getText()])
                    w.writerow([url.get('href')])
                    w.writerow([user.getText()])
                else:
                    next

url = "http://b.hatena.ne.jp/"
Scraper(url).scrape()