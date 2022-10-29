import aiohttp
import asyncio
import time

urls = [
  f'https://www.cnblogs.com/#p{page}'
  for page in range(1, 10 + 1)
]


async def async_crawl(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      res =  await response.text()
      print(f'Crawl url and len of res: {url}, {len(res)}')


loop = asyncio.get_event_loop()

tasks = [
  loop.create_task(async_crawl(url))
  for url in urls
]

# amain with loop
start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f'Async total time: {end - start}')
