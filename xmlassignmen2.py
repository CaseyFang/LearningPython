import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter URL: ")
if len(url)<1:
    url = 'http://py4e-data.dr-chuck.net/comments_211125.xml'

uh=urllib.request.urlopen(url,context=ctx)   
data = uh.read()

print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
lst=tree.findall('comments/comment')
print('Count', len(lst))
counts = 0
for item in lst:
#    print('Name', item.find('name').text)
    counts=counts+float(item.find('count').text)

print('Sum: ',int(counts))