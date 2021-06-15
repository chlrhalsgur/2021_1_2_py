from tkinter import *
import tkinter.ttk  # Treeview 메서드(table 관련)
# import table_test
from functools import partial

import webbrowser #url연결 네이버 영화 보여줄 때 사용


#from tkhtmlview import HTMLLabel  //html사용해서 네이버영화, 네이버영화랭킹링크 사용할려고 했음 but 안됨
#https://remixicon.com/    사용할려고 했던 아이콘



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

#뒤로가기 버튼
def back_and_close():
    win.quit  

def sort_list(movie_list, value):
    sorted_list = sorted(movie_list, key=lambda movie_list: movie_list[value])
    return sorted_list


# print(sort_list(movie_list, 2))
win=Tk()


#새로운 윈도우 열고, 3개의 메뉴 보여줌
def create_window(movie_list, movie_list_r):
    window = Toplevel(win) #새로운 창 열기
    window.geometry("1000x600")
    window.configure(bg='#4682B4')
    btn = Button(window, text = "Show Movie", command = partial(Naver_movie, movie_list))
    btn1 = Button(window, text = "Show Movie Ranking", command= partial(Naver_movie_Ranking, movie_list))
    btn2 = Button(window, text = "Our New Movie Ranking", command= partial(Our_new_Ranking, movie_list_r))

    
    button = Button(window,text = "<<back", command = window.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"))
    button.place(relx=0.8, rely=0.9)

    btn.pack(pady=40)
    btn1.pack(pady=20)
    btn2.pack(pady=20)

def  Click_and_Quit():
  win.geometry("100x50")
  


#Show Movie 클릭했을 경우 네이버 영화 사이트에 들어가서 상영영화 보여주기
def Naver_movie(movie_list):
    url="https://movie.naver.com/"
    webbrowser.open(url)
    

#Show Movie Ranking 클릭했을 경우 네이버 영화 랭킹 보여주기
def Naver_movie_Ranking(movie_list):
    # GUI창을 생성하고 라벨을 설정한다.
    root=tkinter.Tk()
    root.title("Our new Movie Ranking")
    root.geometry("1000x600")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="Our new Movie Ranking") # 제목
    lbl.pack() 

    # 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three"], displaycolumns=["one","two","three"], height = 300)
    treeview.pack()

    button = Button(root,text = "<<back", command = root.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"))
    button.place(relx=0.8, rely=0.9)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=100,)
    treeview.heading("#0", text="index")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="Title", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Rate", anchor="center")

    treeview.column("#3", width=70, anchor="center")
    treeview.heading("three", text="Genre_code", anchor="center")


    # 표에 데이터 삽입
    for i in range(len(movie_list)):
        treeview.insert('', 'end', text=i, values=movie_list[i], iid=str(i)+"번")

    # GUI 실행
    root.mainloop()


#Our New Movie Ranking 클릭했을 경우 새로운 랭킹 보여주기
def Our_new_Ranking(movie_list_r):
    # GUI창을 생성하고 라벨을 설정한다.
    root=tkinter.Tk()
    root.title("Naver Movie Ranking")
    root.geometry("1000x600")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="Naver Movie Ranking") # 제목
    lbl.pack() 

    button = Button(root,text = "<<back", command = root.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"))
    button.place(relx=0.8, rely=0.9)


    # 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three"], displaycolumns=["one","two","three"], height = 300)
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=100)
    treeview.heading("#0", text="index")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="Title", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Rate", anchor="center")

    treeview.column("#3", width=70, anchor="center")
    treeview.heading("three", text="G33333333333333333333e", anchor="center")

    # 스크롤바 
    treeview.yview()

    # 표에 데이터 삽입
    for i in range(len(movie_list_r)):
        treeview.insert('', 'end', text=i, values=movie_list_r[i], iid=str(i)+"번")

    # 버튼 생성 
    btn_back = Button(root, width=10, height=3, padx=5, pady=10, fg = 'red', bg='yellow', text='Back', command=create_window) # 버튼 생성 (창선택, size, padding, style, text, command)
    btn_back.place(x=800, y = 300)
    btn_back.pack() # 버튼 적용

    


    # GUI 실행
    root.mainloop()
# Our_new_Ranking(movie_list_r)
#두 번째 페이지


def make_front(movie_list, movie_list_r):
    win.geometry("1000x600")  #사이즈 가로x세로(픽셀)
    win.title("Movie Ranking") #타이틀
    win.option_add("*Font","Courier 40") #기본 폰트와 글자크기 설정

    #첫 번째 페이지
    lab=Label(win, text = "Pop Corn Movie")
    lab.pack(side=TOP, pady=60)
    lab.configure(font=("Courier", 70, "italic"))

    #첫 번째 페이지 버튼
    btn = Button(win, text="Let's start", command = partial(create_window, movie_list, movie_list_r))
    btn.pack(side=BOTTOM, pady=50)

    button = Button(win,text = "<<Quit", command = win.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"))
    button.place(relx=0.8, rely=0.9)

    #배경색
    win.configure(bg='#49A')

    win.mainloop() #창 열기

make_front(movie_list, movie_list_r)