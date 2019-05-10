import urllib.request, urllib.parse, urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter URL: ")
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_211126.json'

uh=urllib.request.urlopen(url,context=ctx)   
data = uh.read()

print(url)
print(len(data))

info = json.loads(data)
print('User count:', len(info["comments"]))
count =0
for item in info["comments"]:
    count =count +float(item['count'])
print(int(count))