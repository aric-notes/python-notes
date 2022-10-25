import requests
import time

urls = [
  f'https://www.cnblogs.com/#p{page}'
  for page in range(1, 50 + 1)
]


def single_spider(url):
  res = requests.get(url)
  print(url, len(res.text))


if __name__ == '__main__':
  # calc duraiton:
  start = time.time()
  for url in urls:
    single_spider(url)

  end = time.time()
  # 5.181910991668701
  print('duration: ', end - start)
