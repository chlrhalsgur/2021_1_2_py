import pymysql

USER = 'root'
PORT = 3306
PWD = '0000'
HOST = 'localhost'

# sql 접속
# conn = pymysql.connect(host='localhost', user = 'root', password = '0000', db='football_players', charset = 'utf8')

'''
입력
접속 -> 커서잡고 -> 쿼리문 작성 -> excute -> commit -> 종료
'''
def input_db(database, table, title, point, genre_code, detail_link, u = USER, P = PORT, p = PWD, h = HOST):
    conn = pymysql.connect(host=h, port = P, user = u, password = p, db=database, charset = 'utf8')
    curs_input = conn.cursor()
    sql_input = f'insert ignore into {table}(title, point, genre_code) values(%s, %s, %s)'
    curs_input.execute(sql_input, (title, point, genre_code))
    conn.commit()
    conn.close()

'''
출력
커서 잡고(딕셔너리) -> 쿼리문 -> excute -> fetch -> 출력
'''
def print_db():
    movie_list = []
    conn = pymysql.connect(host=HOST, port = PORT, user = USER, password = PWD, db='movie_list', charset = 'utf8')
    curs_output = conn.cursor(pymysql.cursors.DictCursor)
    sql_output = 'select * from movie_table' 
    curs_output.execute(sql_output)
    movie = curs_output.fetchall()

    for row in movie:
        movie_list.append([row['title'], row['point'], row['genre_code']])
    conn.close()
    return movie_list
    
# print(print_db())


# sql 종료
# conn.close()