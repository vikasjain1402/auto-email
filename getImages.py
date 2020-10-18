url="https://source.unsplash.com/1900x1400/?"
import requests
import imghdr
import os

category=["science","kid","school","technolgy","fashion","nature","water","fire","boy","girl","beach","fruit"]
from itertools import combinations
a=combinations(category,2)

downloadpath="/home/vikas/Desktop/"
for i in a:
    urls=url+",".join(i)
    data=requests.get(urls)
    if data.status_code==200:
        filename=os.path.join(downloadpath,"-".join(i)+".jpeg")
        with open(filename,"wb") as a:
            a.write(data.content)
            break
