import os
import requests
import time
import random

origin_url = 'http://map.geoq.cn/arcgis/rest/services/ChinaOnlineStreetPurplishBlue/MapServer/tile/'
def getImageByUrl(z, y, x):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 SE 2.X MetaSr 1.0',
        'Referer': 'http://map.geoq.cn/arcgis/rest/services/ChinaOnlineStreetPurplishBlue/MapServer'
    }
    url = origin_url + str(z) + '/' + str(y) + '/' + str(x)
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
        filePath = 'images/' + str(z) + '/' + str(y) + '/' + str(x) + '.png'
        os.makedirs(os.path.dirname(filePath), exist_ok=True)
        with open(filePath, mode='wb') as f:
            f.write(response.content)
        print(url + '--------> download success!')
    elif response.status_code == 404:
        print(url + '--------> is not found!')
    else:
        print(url + '--------> occurred error!')

Z_max = 16
xs = [0, 1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191, 16383, 32767, 65535, 131071, 262143, 524287]
ys = [1, 2, 5, 10, 20, 40, 80, 160, 321, 642, 1284, 2569, 5138, 10277, 20555, 41111, 82222, 164444, 328888, 657776]

Y_max = ys[Z_max] + 1 #p ow(2, Z_max + 1)
X_max = xs[Z_max] + 1 # pow(2, Z_max)
k = Z_max
# for k in range(0, Z_max):
for i in range(54101, 54105): # X_max
    for j in range(25012, 25016): # 0, Y_max
        # url_ijk = origin_url + str(k) + '/' + str(j) + '/' + str(i)
        # print(url_ijk)
        random_number = random.uniform(0.02, 0.12)
        time.sleep(random_number)
        getImageByUrl(k, j, i)