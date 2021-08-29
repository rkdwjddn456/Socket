import socket
import sys

HOST = '192.168.0.4'
PORT = 5678

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
client_socket.sendall('start'.encode())

data = client_socket.recv(1024)

client_socket.sendall('end_1'.encode())

client_socket.close()