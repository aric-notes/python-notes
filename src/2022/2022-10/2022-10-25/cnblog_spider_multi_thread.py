import requests
import time
import threading

urls = [
  f'https://www.cnblogs.com/#p{page}'
  for page in range(1, 50 + 1)
]


def single_spider(url):
  res = requests.get(url)
  print(url, len(res.text))


def multi_thread_spider(urls):
  threads = []
  for url in urls:
    t = threading.Thread(target=single_spider, args=(url,))
    t.start()
    threads.append(t)

  for t in threads:
    t.join()


if __name__ == '__main__':
  # calc duraiton:
  start = time.time()
  multi_thread_spider(urls)
  end = time.time()
  # 2.0455682277679443
  print('duration: ', end - start)
