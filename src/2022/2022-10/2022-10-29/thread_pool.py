import concurrent.futures
import requests
from bs4 import BeautifulSoup

urls = [
  f'https://www.cnblogs.com/#p{page}'
  for page in range(1, 4 + 1)
]

def crawl(url):
  html = requests.get(url).text
  print(f'current urls is :{url}')
  return html

def parse(html):
  soup = BeautifulSoup(html, 'html.parser')
  return soup.title.text

def main():
  with concurrent.futures.ThreadPoolExecutor() as executor:
    htmls = executor.map(crawl, urls)
  print('crawl done')

  with concurrent.futures.ThreadPoolExecutor() as executor:
    urls_htmls = zip(urls, htmls)
    futures = {}
    for url, html in urls_htmls:
      future = executor.submit(parse, html)
      futures[future] = url

    # 顺序的输出
    # for future, url in futures.items():
    #   print(f'{url}: {future.result()}')

    # 无序的输出
    for future in concurrent.futures.as_completed(futures):
      url = futures[future]
      print(f'{url}: {future.result()}')

  print('parse done')

if __name__ == '__main__':
  main()
