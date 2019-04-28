name =input("Enter file: ")
if len(name) < 1: 
    name = "mbox-short.txt"
fhand = open(name)
lst=list()

#create a list with hours of line start with From

for line in fhand:
    if not line.startswith("From "):
        continue
    else:
        x=line.split()
        lst.append(x[5]) 

ls=list()
for y in lst:
    y=y.split(":")
    ls.append(y[0])

#create dictionary of hour and its count
counts = dict()   
l=list()
for hr in ls:
    counts[hr]=counts.get(hr,0)+1

#sort list of dictionary
z=sorted(counts.items())
for k,v in z:
    print(k,v)




