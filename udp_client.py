import socket

target_host = 'localhost'
target_port = 2345


#SOCKET__aF_INET=IPV4

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


client_socket.sendto("GET / HTTP/1.1\r\nHost:www.time.ir\r\n\r\n", (target_host, target_port))

#4096 toleshe

response = client_socket.recvfrom(4096)



print response

raw_input("please enter to continue")