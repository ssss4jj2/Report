"""
 Project : 파이썬 프로그램 Homework 8.1
 Author  : 21611845 이승준
 Date of last update : 2020 11 5
 Update list : 
      
"""
#Procedure Drawing polygons with turtle

# import turtle

# turtle.title("Drawing polygons with turtle") # 터틀그래픽 윈도우 제목 지정
# turtle.setup(600,500) # 창크기 지정
# turtle.mode("standard")
# t = turtle.Turtle()
# t.pensize(2)
# t.up(); t.shape(name='classic'); t.down()
# radius = 50

# # 다각형들을 튜플로 지정 (pos_x,pos_y,color,num_vertices)
# polygons = [(-225, 150, "red", 3), (-75, 150, "blue", 4), (75, 150, "green", 5),\
#             (225, 150, "magenta", 6), (-225, -50, "brown", 7),\
#             (-75, -50, "chocolate", 8),(75, -50, "black", 9),\
#             (225, -50, "indigo", 0)]

# for i in range(len(polygons)):
#     (pos_x, pos_y, shape_color, num_vertices) = polygons[i]
#     t.up(); t.goto(pos_x, pos_y); t.down()
#     t.dot(10,'red');t.write((pos_x,pos_y)) # 다각형의 중심좌표 점 찍기
#     t.up(); t.goto(pos_x, pos_y+radius); t.setheading(180); t.down() # 중심좌표에서 y축으로 반지름만큼 더 가서 시작
#     t.color(shape_color)
#     if num_vertices > 2: # 삼각형 이상
#         t.circle(radius, steps = num_vertices)
#     else: # 원 일때 
#         t.circle(radius)


"""
 Project : 파이썬 프로그램 Homework 8.2
 Author  : 21611845 이승준
 Date of last update : 2020 11 5
 Update list : 
      
"""
#Procedure  마우스 이벤트를 이용하여 왼쪽버튼은 붉은선, 오른쪽은 푸른선

# import turtle

# board = turtle.Screen()
# board.screensize(800,600,'light blue') # 터틀 스크린 창 설정.

# pointer = turtle.Turtle() # 터틀 객체의 포인터 생성 및 지정
# pointer.color('red')
# pointer.pencolor('red')
# pointer.ht()

# def teleport_btn1(x,y): # 마우스 왼쪽을 누를때, 빨간선 생성
#     pointer.pencolor('red') 
#     pointer.goto(x,y)
#     pointer.dot(10, "red")
#     pointer.write((pointer.xcor(), pointer.ycor()))
    
# def teleport_btn3(x,y): # 마우스 오른쪽을 누를때, 파란선 생성
#     pointer.pencolor('blue') 
#     pointer.goto(x,y)
#     pointer.dot(10, "blue")
#     pointer.write((pointer.xcor(), pointer.ycor()))
    
# def quitThis():
#     board.bye()
    
# board.onclick(teleport_btn1, btn=1) # 마우스 왼쪽을 누를때
# board.onclick(teleport_btn3, btn=3) # 마우스 오른쪽을 누를때
# board.onkey(quitThis,'q')

# board.listen() # 터틀스크린에서 키보드 이벤트 받을 수 있도록 대기
# board.mainloop() 


"""
 Project : 파이썬 프로그램 Homework 8.3
 Author  : 21611845 이승준
 Date of last update : 2020 11 5
 Update list : 
      
"""
#Procedure km와 mile의 양방향 계산기 구현

# from tkinter import*

# class App:
#     def __init__(self,master):
#         frame = Frame(master)
#         frame.pack()
        
#         # Km의 값을 받음
#         Label(frame,text = 'Km').grid(row = 0, column =1)
#         self.c_var = DoubleVar()
#         Entry(frame, textvariable=self.c_var).grid(row=0, column=0)
#         # Mile의 값을 받음
#         Label(frame, text='Mile').grid(row=0, column=3)
#         self.c_var2 = DoubleVar()
#         Entry(frame, textvariable=self.c_var2).grid(row=0, column=2)
        
#         # km -> Mile 버튼
#         button = Button(frame, text='km -> Mile', command=self.convert_KtoM)
#         button.grid(row=2, column=0)
#         # Mile -> km 버튼
#         button2 = Button(frame, text='Mile -> km', command=self.convert_MtoK)
#         button2.grid(row=2, column=2)
        
        
#     def convert_KtoM(self): # Km를 Mile로 변환
#         c= self.c_var.get()
#         self.c_var2.set(c/1.609344)   

#     def convert_MtoK(self): # Mile을 Km로 변환
#         c= self.c_var2.get()
#         self.c_var.set(c*1.609344)   
        
# window =Tk()
# window.wm_title('Km <-> Mile Converter')
# app = App(window)
# window.mainloop()


"""
 Project : 파이썬 프로그램 Homework 8.4
 Author  : 21611845 이승준
 Date of last update : 2020 11 5
 Update list : 
      
"""
#Procedure 스톱워치를 tkinter GUI 프로그램으로 구현

# import time
# from tkinter import*


# def runTimer(): # 시간 표현
#     global start_time,elapsed_time,prev_elapsed_time
#     if(running): # 스탑워치가 running일때
#         cur_time = time.time()
#         time_diff = cur_time - start_time # 현재 시각에서 시작시간을 뻄
#         elapsed_time = time_diff + prev_elapsed_time 
#         timeText.configure(text="{:7.3f}".format(elapsed_time)) # 소수점 3째 자리 까지
#     window.after(10, runTimer)
    
# def start(): # Start 버튼 함수.
#     global running, start_time, elapsed_time, prev_elapsed_time
#     if(running != True):
#         running = True
#         start_time = time.time()
#         prev_elapsed_time  = elapsed_time

# def stop(): # Stop 버튼 함수.
#     global running, prev_elapsed_time, elapsed_time
#     running = False
#     prev_elapsed_time = elapsed_time

# def reset(): # Reset 버튼 함수.
#     global running, start_time, elapsed_time, prev_elapsed_time
#     running = False
#     elapsed_time = 0.0 # 초기화 시킴.
#     prev_elapsed_time = 0.0
#     timeText.configure(text="{:7.3f}".format(elapsed_time))

# #------------------

# window = Tk()
# window.title("21611845 Stop watch") # 윈도우 제목

# running = False
# start_time  = stop_time = time.time()
# prev_elapsed_time = elapsed_time = 0.0 # 글로벌 변수 초기화
# # timeText 레이블 생성( 폰트 크기의 굵은 40 Arial체)
# timeText = Label(window, height = 5, text="0",font=("Arial 40 bold"))
# timeText.pack(side = TOP)
# # Start 버튼
# startButton = Button(window, width=10, text="Start",bg="green", command=start)
# startButton.pack(side = LEFT) # LEFT를 함으로써 한줄에 차례대로 설치
# # Stop 버튼
# stopButton = Button(window, width=10, text="Stop",bg="red", command=stop)
# stopButton.pack(side = LEFT)
# # Reset 버튼
# resetButton = Button(window, width=10, text="Reset",bg="yellow", command=reset)
# resetButton.pack(side = LEFT)

# if __name__ == '__main__':
#     runTimer()
#     window.mainloop()


"""
 Project : 파이썬 프로그램 Homework 8.5
 Author  : 21611845 이승준
 Date of last update : 2020 11 5
 Update list : 
      
"""
#Procedure 600 x 400 픽셀 크기 테이블에서 공 튀기기 구현

import tkinter 
from tkinter import*
from tkinter import messagebox

def ask_quit():
    result = messagebox.askquestion("Mesage", "Quit")
    if result == "yes":
        window.destroy()
        
def change_direction(event):
    global DX, DY
    if event.keysym == "Left": # 왼쪽 방향키 누르면 왼쪽으로
        DX = -STEP; DY =0 
    elif event.keysym == "Right": # 오른쪽 방향키 누르면 오른쪽으로
        DX = STEP; DY =0
    elif event.keysym == "Up": # 위 방향키 누르면 위으로
        DX = 0; DY =-STEP
    elif event.keysym == "Down": # 밑 방향키 누르면 밑으로
        DX = 0; DY = STEP
    elif event.keysym == "Escape": # esc 키를 누르면 45도 이동
        DX = STEP; DY =STEP
    else:
        DX = STEP; DY = STEP
        
def init():
    global window, canvas,DX,DY,STEP
    window=Tk()
    window.title("Bouncing ball with direction change")
    canvas = Canvas(window, width=600, height=400)
    canvas.pack(expand=YES, fill=BOTH)
    canvas.create_oval(80, 80, 120, 120, fill="red", tag="Ball") # 지름이 80인 볼 생성.
    STEP = 1
    DX = STEP
    DY = STEP
    window.protocol("WM_DELETE_WINDOW", ask_quit)
    window.bind("<Left>", change_direction)
    window.bind("<Right>", change_direction)
    window.bind("<Up>", change_direction)
    window.bind("<Down>", change_direction)
    window.bind("<Escape>", change_direction)
    
def animate():
    global DX, DY
    Delay = 5 # 5밀리초의 지연시간
    canvas.move("Ball", DX, DY) 
    pos = canvas.coords("Ball")
    if pos[0] < 0 or pos[2] > canvas.winfo_width():
        DX *=-1 # x축 상의 방향을 반대로 함
    if pos[1] < 0 or pos[3] > canvas.winfo_height():
        DY *=-1 # y축 상의 방향을 반대로 함
    canvas.update_idletasks()
    canvas.update()
    canvas.after(Delay, animate) # 5밀리초 후회 animate함
    
if __name__ == '__main__':
    init()
    animate()
    mainloop()
    change_direction(event)