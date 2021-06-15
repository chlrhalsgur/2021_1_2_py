import crawling_test3 as crw
import db_test1
import Rerating_movie
from datetime import datetime
import new_front

movie_list = [
    ['홀리데이', '8.67', 16],
    ['화차', '8.3018', 13],
    ['화차', '8.3018', 13],
    ['환생', '8.181', 2],
    ['후크', '9.12', 12],
    ['휴고', '7.78', 12],
    ['히든 페이스', '8.01', 7],
    ['히든 피겨스', '9.99', 1],
    ['히트', '9.11', 16]
]


movie_list_r = [
    ['홀리데이', '8.112', 16],
    ['화차', '8.1238', 13],
    ['화차', '8.12318', 13],
    ['환생', '8.4353', 2],
    ['후크', '9.112', 12],
    ['휴고', '7.998', 12],
    ['히든 페이스', '8.29124', 7],
    ['히든 피겨스', '9.18259999999', 1],
    ['히트', '9.12431', 16]
]


# print(datetime.today())
crw.crawling_movie()
movie_list = db_test1.print_db() 
movie_list_r = Rerating_movie.rerate(movie_list)

new_front.make_front(movie_list, movie_list_r)

