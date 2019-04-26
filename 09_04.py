name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = list()
words = dict()

for line in handle:
    if not line.startswith("From"):
        continue
    else:
        x=line.split()
        lst.append(x[1])

for sender in lst:
    words[sender]=words.get(sender,0)+1

bigcount = None
bigword = None
for word,count in words.items():
    if bigcount is None or count>bigcount:
        bigword=word
        bigcount=count

print(bigword,bigcount)
