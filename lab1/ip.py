import csv 
from io import StringIO
file = ''

with open("file.txt") as f:
    file = f.readlines()[1:]

r = csv.reader(StringIO("".join(file)))
src = set()
dst = set()

for row in r:
    src.add(row[2])
    dst.add(row[3])


print("Source: ", src)
print("Destination:", dst)

import subprocess

for ip in (list(src) + list(dst)):
    result = subprocess.run(["whois", ip], capture_output=True, text=True)

    for line in result.stdout.splitlines():
        if "orgname" in line.lower():
            print(line, ip)