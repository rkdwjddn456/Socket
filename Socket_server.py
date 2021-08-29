import time
import sys
import socket
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

HOST = '192.168.0.4'
#HOST = '172.30.1.9'
PORT = 5678

Button1_Count = 0
Button2_Count = 0

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

client_socket, addr = server_socket.accept()
print('Connected by', addr)

class Thread1(QThread):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print("robot button1 is start")

        global Button1_Count

        if Button1_Count == 0:
            while True:
                
                data = client_socket.recv(1024)
                
                print('(start)Received from', addr, data.decode())
                data_1 = "1"
                client_socket.sendall(bytes(data_1.encode()))  
                if data.decode() == "start":
                    print("start_1")
                    break                         
                
            while True:
                data = client_socket.recv(1024)
                if data.decode() == "end_1":
                    Button1_Count = Button1_Count + 1
                    print('(finish)Received from', addr, data.decode())
                    print("end_1")                   
                    break
                
            print("button1 loop finish")
            
        elif Button1_Count == 1:
            while True:
                
                data = client_socket.recv(1024)
                
                print('(start)Received from', addr, data.decode())
                data_1 = "2"
                client_socket.sendall(bytes(data_1.encode()))  
                if data.decode() == "start":
                    print("start_2")
                    break                         
                
            while True:
                data = client_socket.recv(1024)
                if data.decode() == "end_2":
                    Button1_Count = Button1_Count + 1
                    print('(finish)Received from', addr, data.decode())
                    print("end_2")                   
                    break
                
            print("button1 loop finish")
            
class Thread2(QThread):

    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent

    def run(self):
        print("robot button2 is start")

        global Button2_Count

        if Button2_Count == 0:      
            while True:
                data = client_socket.recv(1024)
                
                print('(start)Received from', addr, data.decode())
                data_2 = "3"
                client_socket.sendall(bytes(data_2.encode()))  
                if data.decode() == "start":
                    print("start_3")
                    break                         
                
            while True:
                data = client_socket.recv(1024)
                if data.decode() == "end_3":
                    Button2_Count = Button2_Count + 1
                    print('(finish)Received from', addr, data.decode())
                    print("end_3")                   
                    break

        elif Button2_Count == 1:
            while True:
                data = client_socket.recv(1024)
                
                print('(start)Received from', addr, data.decode())
                data_2 = "4"
                client_socket.sendall(bytes(data_2.encode()))  
                if data.decode() == "start":
                    print("start_4")
                    break                         
                
            while True:
                data = client_socket.recv(1024)
                if data.decode() == "end_4":
                    Button2_Count = Button2_Count + 1
                    print('(finish)Received from', addr, data.decode())
                    print("end_4")                   
                    break

            print("button2 loop finish")
        

class MainWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        btn1 = QPushButton("버튼1 시작")
        btn1.clicked.connect(self.robotButton1)
        btn1.setCheckable(True)

        btn2 = QPushButton("버튼2 시작")
        btn2.clicked.connect(self.robotButton2)
        btn2.setCheckable(True)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)

        #self.resize(200,200)
        self.setLayout(vbox)
        self.setWindowTitle('Robot Button')
        self.setGeometry(300,300,300,200)

    def robotButton1(self):
        x1 = Thread1(self)
        x1.start()

    def robotButton2(self):
        x2 = Thread2(self)
        x2.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MainWidget()
    widget.show()
    sys.exit(app.exec_())