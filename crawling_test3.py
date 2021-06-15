from re import findall
from pymysql import connections
import requests
from bs4 import BeautifulSoup
from soupsieve import select_one
import db_test1
from datetime import datetime

USER = 'root'
PORT = 3306
PWD = '0000'
HOST = 'localhost'

date = datetime.today().strftime("%Y%m%d")

def crawling_movie():
    for genre_code in range(1,20):
        if genre_code == 9 or genre_code == 3:
            continue
        date = '20210525'
        url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date={date}&tg={genre_code}'
        headers = {"User-Agent":"Mozilla/5.0"}

        res = requests.get(url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text,'lxml') 
        title = soup.select('td.title > div.tit5 > a')
        point = soup.select('td.point') 
        detail_link = soup.select('td.ac > a')

        for t, p in zip(title, point):
            
            db_test1.input_db('movie_list', 'movie_table', t.getText(), float(p.getText()), genre_code, detail_link, USER, PORT, PWD, HOST)
    
# crawling_movie()
