import urllib.request
from urllib.parse import urljoin  # URLを扱うモジュールを追加
from bs4 import BeautifulSoup as BS

class Scraper:
    def __init__(self, site):
        self.site = site
        self.urls = set()  # 収集済みURLを入れておく変数

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BS(html, parser)
        for tag in sp.find_all('a'):
            url = tag.get('href')
            if url is None:
                continue
            if 'atcl/news' not in url:  # 'atcl/news' を含まないURLは対象外にする
                continue
            full_url = urljoin(self.site, url)  # ドメイン名を含むURLに変換
            if full_url in self.urls:  # 既に収集済みのURLは対象外にする
                continue
            self.urls.add(full_url)  # 収集済みURLに追加
            print('\n' + full_url)  # URLを表示


news = 'https://trendy.nikkeibp.co.jp/news/'  # ニュース取得元サイトを変更
Scraper(news).scrape()
