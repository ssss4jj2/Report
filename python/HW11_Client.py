"""
 Project : 파이썬 프로그램 Homework 11.1
 Author  : 21611845 이승준
 Date of last update : 2020 11 26
 Update list : 
      
"""
#Procedure 파이썬 스레드 기반의 채팅 프로그램 구현

import socket, sys, threading
from threading import Thread # for testing multi-thread
from time import sleep #for sleep in thread
import tkinter as tk
from tkinter import ttk, scrolledtext, END
LocalHost = "127.0.0.1"
SocketChat_PortNumber = 50000

class socketChatting:
    def __init__(self,mode):
        global hostAddr
        #create instance
        self.win=tk.Tk() # 윈도우 생성
        self.mode=mode#server or client
        
        # Add a title 
        self.win.title("Multi-thread-based Socket Chatting (TCP Client)")
        hostname = socket.gethostname()
        hostAddr = socket.gethostbyname(hostname)
        print("My (client) IP address = {}".format(hostAddr)) # 내 ip주소 반환
        self.myAddr = hostAddr
        self.createWidgets()
        
        cli_thread = Thread(target=self.TCPClient, daemon=True) # 스레드 생성
        cli_thread.start()
        
    # TCP client
    def TCPClient(self):
        self.cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 생성
        servAddr_str = input("Server IP Addr (e.g., '127.0.0.1') = ") # 서버 ip 주소를 입력
        self.cliSock.connect((servAddr_str, SocketChat_PortNumber))  # 연결됨
        
            # send connect request to TCP server
        servAddr = self.cliSock.getpeername() # 서버 쪽의 주소를 알수 있음
        print("TCP Client is connected to server ({})\n".format(servAddr))
        self.scr_cliDisplay.insert(tk.INSERT,"TCP client is connected to server \n")
        self.scr_cliDisplay.insert(tk.INSERT,"TCP server IP address : {}\n".format(servAddr[0]) )
        self.servAddr_entry.insert(END, servAddr[0])
        while True:
            cliRecvMsg = self.cliSock.recv(8192).decode() # 메세지를 받아 디코드한다
            if not cliRecvMsg:
                break
            self.scr_cliDisplay.insert(tk.INSERT,">>"+cliRecvMsg) # 서버에서 보낸 메세지 출력
        self.cliSock.close()
        
    # Exit GUI cleanly; definition of quit()
    def _quit_(self): # 윈도우 종료
        self.win.quit()
        self.win.destroy()
        exit()
        
    # Modified Button Click Function
    def connect_server(self):
        self.scr_cliDisplay.insert(tk.INSERT,"Connecting to server ....")
        self.myIpAddr = self.myAddr.get()
        self.peerIpAddr = self.peerAddr.get()
        self.scr_cliDisplay.insert(tk.INSERT, "My IP Address : " + self.myIpAddr + '\n')
        self.scr_cliDisplay.insert(tk.INSERT, "Server's IP Address : " + self.peerIpAddr + '\n')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.peerIpAddr, SocketChat_PortNumber))  # 연결을 하게끔 해줌
            # send connect request to TCP server 
            
    #define callback for myMsg_enter()
    def cli_send(self): #from mySelf to peer/server
        msgToServer = str(self.scr_cliInput.get(1.0, END))  # 내용들을 받아 저장
        self.scr_cliDisplay.insert(tk.INSERT,"<< " + msgToServer) # 내가 보낸 내용도 표시
        self.cliSock.send(bytes(msgToServer.encode())) # 소켓을 통해 보냄
        self.scr_cliInput.delete('1.0', END) #clear scr_msgInput scrolltext
        
    def createWidgets(self):
        # Add a frame in self.win
        frame = ttk.LabelFrame(self.win, text="Frame (Socket-based Text Message Chatting)")
        frame.grid(column=0, row=0, padx=8, pady=4)
        
        #Add a LabelFrame of myAddr, peerAddr, Connect Button in frame
        frame_addr_connect = ttk.LabelFrame(frame, text="")
        frame_addr_connect.grid(column=0, row=0, padx=40, pady=20, columnspan=2)
        
        # Add labels (myAddr, peerAddr) in the frame_addr_connect
        myAddr_label = ttk.Label(frame_addr_connect, text="MyAddr (Client)")
        myAddr_label.grid(column=0, row=0, sticky='W') #
        peerAddr_label = ttk.Label(frame_addr_connect, text="Server Addr")
        peerAddr_label.grid(column=1, row=0, sticky='W') #
        
        # Add a Textbox Entry widgets (myAddr, peerAddr) in the frame_addr_connect
        self.myAddr = tk.StringVar()
        self.myAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable=self.myAddr) # fram_addr_connect부분에 Entry생성
        self.myAddr_entry.insert(END, hostAddr) 
        self.myAddr_entry.grid(column=0, row=1, sticky='W')
        
        self.servAddr = tk.StringVar()
        self.servAddr_entry = ttk.Entry(frame_addr_connect, width=15, textvariable="")
        #self.servAddr_entry.insert(END, LocalHost)
        self.servAddr_entry.grid(column=1, row=1, sticky='W')
        
        # Add a connect_button
        connect_button = ttk.Button(frame_addr_connect, text="Connect",command=self.connect_server) 
        connect_button.grid(column=3, row=1)
        connect_button.configure(state='enable') # for local  # 사용하려면, enable로 변경
        #connect_button.configure(state='disabled') # for local  # 사용하려면, enable로 변경
        
        # Add ScrolledText fields of display and input 
        cliDisplay_label = ttk.Label(frame, text="Socket Client Display")
        cliDisplay_label.grid(column=0, row=1 )
        scrol_w, scrol_h = 40, 20
        self.scr_cliDisplay = scrolledtext.ScrolledText(frame, width=scrol_w,\
            height=scrol_h, wrap=tk.WORD)
        self.scr_cliDisplay.grid(column=0, row=2, sticky='WE') #, columnspan=3
        
        cliInput_label = ttk.Label(frame, text="Input Text Message (Client) :")
        cliInput_label.grid(column=0, row=3 )
        
        self.scr_cliInput = scrolledtext.ScrolledText(frame, width=40, height=3, wrap=tk.WORD)
        self.scr_cliInput.grid(column=0, row=4) #, columnspan=3
        
        # Add Buttons (cli_send, serv_send)
        cli_send_button = ttk.Button(frame, text="Send Message to Server", command=self.cli_send)  # send버튼 생성
        cli_send_button.grid(column=0, row=5, sticky='E')
        
        #Place cursor into the message input scrolled text
        self.scr_cliInput.focus()
    
#======================
# Start GUI
#======================
print("Running TCP Client")
sockChat = socketChatting("Client")
sockChat.win.mainloop()