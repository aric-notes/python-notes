import time
import concurrent.futures

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
  start = time.time()
  for n in range(2, 1000):
    is_prime(n)
  end = time.time()
  print('single_thread: ', end - start)

def multiple_thread():
  start = time.time()
  with concurrent.futures.ThreadPoolExecutor() as executor:
    for n in range(2, 1000):
      executor.submit(is_prime, n)
  end = time.time()
  print('multiple_thread: ', end - start)

def multiple_process():
  start = time.time()
  with concurrent.futures.ProcessPoolExecutor() as executor:
    for n in range(2, 1000):
      executor.submit(is_prime, n)
  end = time.time()
  print('multiple_process: ', end - start)


if __name__ == '__main__':
  single_thread()
  multiple_thread()
  multiple_process()
