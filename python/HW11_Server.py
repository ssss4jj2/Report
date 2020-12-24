"""
 Project : 파이썬 프로그램 Homework 11.1
 Author  : 21611845 이승준
 Date of last update : 2020 11 26
 Update list : 
      
"""
#Procedure 파이썬 스레드 기반의 채팅 프로그램 구현

import socket, sys, threading
from threading import Thread # for testing multi-thread
from time import sleep # for sleep in thread time에서 sleep기능 사용
import tkinter as tk
from tkinter import ttk, scrolledtext, END
LocalHost = "127.0.0.1" # 자기 자신의 컴퓨터 하나로 하기 위해서 지정.
SocketChat_PortNumber = 50000 # 포트 번호

class SocketChatting:
    def __init__(self,mode):
        global hostAddr
        # Create instance
        self.win=tk.Tk() # 윈도우 하나 생성.
        self.mode=mode # server or client
        
        self.win.title("Multi-thread-based Socket Chatting (TCP Server)") # 윈도우창 타이틀
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname)
        print("My (server) IP address = {}".format(hostAddr)) # 해당하는 컴퓨터의 ip
        self.myAddr = hostAddr
        self.createWidgets() # 창이 구성되게 만듬
        # Start TCP/IP server in its own thread
        serv_thread = Thread(target=self.TCPServer, daemon=True)  # 스레드 생성.
        serv_thread.start()
        
    # TCP server
    def TCPServer(self): # daemon으로 생성된 스레드
        self.servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.servSock.bind((hostAddr, SocketChat_PortNumber)) 
            # bind socket to (IP_addr(local_host), port_number)
        self.scr_servDisplay.insert(tk.INSERT,"TCP server is waiting for a client .... \n" ) # 중간 디스플레이에 메세지 출력
        self.servSock.listen(1) # 서버에서 listen 상태
        self.conn, self.cliAddr = self.servSock.accept() # cliAddr : (IPaddr, port_no), 실제로 데이터를 주고받는 소켓
        print("TCP Server is connected to client ({})\n".format(self.cliAddr))
        self.scr_servDisplay.insert(tk.INSERT,"TCP server is connected to client\n" )
        self.scr_servDisplay.insert(tk.INSERT, "TCP client IP address : {}\n".format(self.cliAddr[0])) # 상대방 ip 주소가 얼마인지.
        self.peerAddr_entry.insert(END, self.cliAddr[0]) # 연결되어 있는 상대방에게 ip를 적음. 0번이 호스트주소, 1번이 포트번호
        
        while True:
            servRecvMsg = self.conn.recv(512).decode() #  한번에 512개의 메세지 받음
            if not servRecvMsg: # 연결 해제 요청시 while을 빠져나감
                break
            self.scr_servDisplay.insert(tk.INSERT,">> " + servRecvMsg) # 메세지 출력
        self.conn.close()
        
    #Exit GUI cleanly; definition of quit()
    def _quit(self):
        self.win.quit() # 윈도우 닫고
        self.win.destroy() # 윈도우삭제
        exit() # 창을 닫음
        
    def serv_send(self): # from server send message to client
        msgToCli = str(self.scr_servInput.get(1.0, END)) # 맨 처음부터 맨 끝까지의 메세지를 읽어 string으로 받음
        self.scr_servDisplay.insert(tk.INSERT,"<< " + msgToCli)
        self.conn.send(bytes(msgToCli.encode())) # 인코딩한 메세지 바이트로 변환 후 전송
        self.scr_servInput.delete('1.0', END) #clear scr_msgInput scrolltext
        
    def createWidgets(self): # 위젯 창 생성 및 설정
        # Add a frame in self.win
        frame = ttk.LabelFrame(self.win, text="Frame (Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4)
        
        #Add a LabelFrame of myAddr, peerAddr, Connect Button in frame
        frame_addr_connect = ttk.LabelFrame(frame, text="")
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)
        
        # Add labels (myAddr, peerAddr) in the frame_addr_connect
        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr(Server)")
        myAddr_label.grid(column=0, row=0, sticky='W') #
        peerAddr_label = ttk.Label(frame_addr_connect, text="Peer(CLient)Addr")
        peerAddr_label.grid(column=1, row=0, sticky='W') #
        
        # Add a Textbox Entry widgets (myAddr, peerAddr) in the frame_addr_connect
        self.myAddr = tk.StringVar() 
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15,\
            textvariable=self.myAddr) # 수정도 가능하게끔
        self.myAddr_entry.insert(END, hostAddr) # 호스트 addr이 자동적으로 표시
        self.myAddr_entry.grid(column=0, row=1, sticky='W')
        self.peerAddr = tk.StringVar()
        self.peerAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        #self.peerAddr_entry.insert(END, LocalHost)
        self.peerAddr_entry.grid(column=1, row=1, sticky='W')
        
        # Add ScrolledText fields of display and input 
        scrol_w, scrol_h = 40, 20
        servDisplay_label = ttk.Label(frame, text="Socket Server Display")
        servDisplay_label.grid(column=0, row=1 )
        self.scr_servDisplay = scrolledtext.ScrolledText(frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr_servDisplay.grid(column=0, row=2, sticky='E') #, columnspan=3
        
        servInput_label = ttk.Label(frame, text="Input Text Message (Server) :")
        servInput_label.grid(column=0, row=3 )
        
        self.scr_servInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD) # 스크롤생성
        self.scr_servInput.grid(column=0, row=4) #, columnspan=3
        
        # Add Buttons (cli_send, serv_send)
        serv_send_button = ttk.Button(frame, text="Send Message to Client", command=self.serv_send) 
        serv_send_button.grid(column=0, row=5, sticky='E')
        
        #Place cursor into the message input scrolled text
        self.scr_servInput.focus()
        
#======================
# Start GUI
#======================
print("Running TCP server")
sockChat = SocketChatting("server")
sockChat.win.mainloop()
