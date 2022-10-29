import time
import concurrent.futures

NUMS = [1232131233] * 100

# 是否为素数
def is_prime(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  max = n ** 0.5 + 1
  i = 3
  while i <= max:
    if n % i == 0:
      return False
    i += 2
  return True

def single_thread():
  for n in NUMS:
    is_prime(n)

def multiple_thread():
  # nums
  with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(is_prime, NUMS)

def multiple_process():
  # nums
  with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(is_prime, NUMS)


if __name__ == '__main__':
  start = time.time()
  single_thread()
  end = time.time()
  print('single_thread: ', end - start)

  start = time.time()
  multiple_thread()
  end = time.time()
  print('multiple_thread: ', end - start)

  start = time.time()
  multiple_process()
  end = time.time()
  print('multiple_process: ', end - start)
