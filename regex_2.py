name = input("Enter File Name: ")
if len(name)<1:
    name = "regex_sum_211121.txt"
fhand = open(name)
total = 0
count = 0
import re

for line in fhand:
    x = line.rstrip()
    y = re.findall('[0-9]+',x)
    for n in y:
        if float(n) > 0:
            total = total + float(n)
            count = count+1
        else:
            continue

print(int(total))