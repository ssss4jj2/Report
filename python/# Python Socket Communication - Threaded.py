# Python Socket Communication - Threaded TCP Streaming Server (1)
import socket
from _thread import *
import time 
import threading

LOCK = threading.Lock()

def thread_Rx(client_socket,addr):
    # repeats until the client disconnects
    while True: 
        try:
            # when message is received from client, just echo the received message
            rx_msg=clien_socket.recv(1024)
            if not rx_msg:
                print('Server::disconnected by client ({}:{})\n'.format(addr[0],addr[1]))
                break
            print('')