import urllib.request
import urllib.parse
import re
import os

dir_main = "D:/Images/H3x"
dir_HT = dir_main + "/HT"
dir_webp = dir_main + "/webps"
dir_webp_new = dir_main + "/webps_new"
dir_img_new = dir_main + "/webps_img_new"

        



headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"


os.chdir(dir_webp)

error_list = []
for filename in os.listdir():
    if filename.find("master1200") != -1:
        print(filename)
        try:
            # Go to pic site
            code = filename[:filename.find("_")]
            url = "https://www.pixiv.net/en/artworks/" + code
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            html = str(resp.read())
            
            # Header 
            headers2 = {
            #     ":authority"    : "i.pximg.net", 
            #     ":method": "GET", 
            #     ":path": "/img-master/img/2010/04/25/05/27/43/10230282_p0_master1200.jpg", 
            #     ":scheme": "https", 
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
                "accept-encoding": "gzip, deflate, br", 
                "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6", 
                "cache-control": "no-cache",
                "dnt"           : "1", 
                "pragma": "no-cache", 
                "referer"       : "https://www.pixiv.net/", 
                "sec-ch-ua-mobile": "?0", 
                "sec-fetch-dest": "document", 
                "sec-fetch-mode": "navigate", 
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",  
                "upgrade-insecure-requests": "1", 
                "user-agent"    : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
            }

            # Get master1200 preview link
            url2 = re.findall(r'\"regular\":\"(.*?)\"', html)[0]
            print(url2)
            req2 = urllib.request.Request(url2, headers=headers2)
            resp2 = urllib.request.urlopen(req)
            extension = url2[url2.rfind('.'):]

            # Write to file
            with open(dir_img_new + "/" + filename[:filename.rfind(".")] + extension, 'wb') as f:
                html = resp2.read()
                f.write(html)
                # print(str(html))
            # os.rename(dir_webp + "/" + filename, dir_webp_new + "/" + filename)
            
        except Exception as e:
            print(e)
            error_list.append(filename)

        break

print(error_list)



