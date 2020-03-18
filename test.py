import requests
import time

r = requests.get('http://20.94201314.net/dm10//ok-comic10/S/27411/act_006/z_0001_60333.JPG')
time.sleep(10)
with open('001.jpg', 'wb') as f:
    f.write(r.content)