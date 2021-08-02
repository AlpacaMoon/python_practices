import urllib.request
import urllib.parse
import re

url = "https://pythonprogramming.net/"
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)

t = open("testfile.txt", 'w')
html = resp.read()
founds = re.findall(r'<p>(.*?)</p>', str(html))
for each in founds:
    t.write(each + '\n')
t.close()
