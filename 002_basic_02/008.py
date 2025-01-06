"""

Write a Python program that retrieves the top stories from Google News.

Link: https://news.google.com/news/rss

Hint:   use `urllib` to open the URL and read the xml contents
        use 'BeautifulSoup` to extract the top stories
        use the 'item' tag to fetch stories and query their 'title', 'link' and 'pubDate'

"""

from bs4 import BeautifulSoup
from urllib.request import urlopen


__google_news = 'https://news.google.com/news/rss'


def main():
    client = urlopen(__google_news)
    xml = client.read()
    client.close()

    page = BeautifulSoup(xml, "xml")
    items = page.findAll("item")

    for _ in items:
        print(_.title.text)
        print(_.link.text)
        print(_.pubDate.text)
        print("=" * 50)


if __name__ == "__main__":
    main()
