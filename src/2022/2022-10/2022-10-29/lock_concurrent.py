import threading
import time


# 账户
class Account:
  def __init__(self, balance):
    self.balance = balance


# 转账
def withdraw(account, amount):
  if account.balance >= amount:
    time.sleep(0.01)
    account.balance -= amount
    print(threading.current_thread().name, "取钱成功，余额为：", account.balance)
  else:
    print(threading.current_thread().name, "取钱失败，余额不足")


if __name__ == "__main__":
  account = Account(1000)
  t1 = threading.Thread(target=withdraw, args=(account, 800), name="t1")
  t2 = threading.Thread(target=withdraw, args=(account, 800), name="t2")
  t1.start()
  t2.start()
  t1.join()
  t2.join()
