record = ('ACME', 50, 123.45, (12, 18, 2012))

name, *_, (*_, year) = record

# python3 src/2020/python3-cookbook/003-discard-rest.py
print(name, year)
