record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

# https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p02_unpack_elements_from_iterables.html

print(name, email, phone_numbers)
# python3 src/2020/python3-cookbook/002-multi-rest.py
