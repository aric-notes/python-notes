import subprocess


output= subprocess.getoutput("ls")

print(
  output.split('\n')
)

# python3 src/2020/2020-09/002-commonds.py
# ['README.md', 'docs', 'package.json', 'src']

