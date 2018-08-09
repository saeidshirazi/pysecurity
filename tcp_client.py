import socket

target_host = 'localhost'
target_port = 2345


#SOCKET__aF_INET=IPV4

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((target_host, target_port))

client_socket.send("GET / HTTP/1.1\r\nHost:www.time.ir\r\n\r\n")

#4096 toleshe

response = client_socket.recv(4096)



print response

raw_input("please enter to continue")