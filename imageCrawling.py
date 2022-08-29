from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import os

baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
plusUrl = input('검색어를 입력하세요 : ')
if (os.path.isdir(f'./downloads/{plusUrl}') == False):
  os.mkdir(f'./downloads/{plusUrl}')

url = baseUrl + quote_plus(plusUrl)
html = urlopen(url)
soup = bs(html, "html.parser")
img = soup.find_all(class_='_img')

n = 1
for i in img:
    imgUrl = i['data-source']
    with urlopen(imgUrl) as f:
        with open(f'./downloads/{plusUrl}/' + plusUrl + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
print('다운로드 완료')