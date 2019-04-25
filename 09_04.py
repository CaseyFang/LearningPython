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
        print(x[1])
        for x[1] in x:
            words[x[1]] = words.get(x[1],0)+1
            print(words)
