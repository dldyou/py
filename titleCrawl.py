from bs4 import BeautifulSoup
import urllib.request
import urllib.parse


while True:
    plusurl = urllib.parse.quote_plus(input('input:'))
    pagenum = 1
    num = input('page: ')

    while (pagenum <= int(num) * 10 - 9):
        url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pagenum}'
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')
    
        title = soup.find_all(class_='api_txt_lines total_tit')
        for i in title:
            print("제목 : " + i.text)
            print("주소 : " + i.attrs['href'])
            print()
        pagenum += 10
