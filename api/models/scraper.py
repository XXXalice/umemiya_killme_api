from bs4 import BeautifulSoup
import requests
import traceback
import sys
from config import TARGET_URL, UA

"""
リクエスト機構
"""
class Crawler:

    def __init__(self):
        self.url = TARGET_URL
        self.send_header = {
            "User-Agent": UA
        }

    def get_html(self):
        """
        とってくる
        :return: htmlソースだよ
        """
        resp = requests.get(url=self.url, headers=self.send_header)
        if resp.status_code != 200:
            try:
                raise Exception
            except:
                traceback.print_exc()
                sys.stdout.write("That's not a normal response.\n")

        return resp.text

    def _save_html(self, html_source):
        import datetime
        """
        htmlの保存を内部で行う
        基本静的なページなので実行の度にリクエストを叩く必要はないため、頻繁なAPIの利用においてはこれで保存したhtmlからスクレイピングする
        :param html_source: アイコンページのhtmlだよ
        :return: ないよ
        """
        file_name = datetime.datetime.now().strftime("%Y%m%d") + "_iconpage.html"
        with open(file_name, "w") as f:
            f.write(html_source)

"""
スクレイピング機構
"""
class Fetcher:

    def __init__(self, html):
        self.html = html

    def scrape_icon(self, num):
        soup = BeautifulSoup(self.html, "html.parser")
        icon_urls = [icon_url
                     for table in soup.find_all("table", class_="td01")
                     for row in table.find_all("tr")
                     for a in row.find_all("img")
                     for icon_url in a["src"]]
        result = None
        import random
        if num == 0:
            result = random.choice(icon_urls)
        else:
            try:
                result = icon_urls[num - 1]
            except IndexError as e:
                result = random.choice(icon_urls)
                
        return result