import socket
import  threading


#0.0.0.0 yani hame ip haye system
listen_ip = '0.0.0.0'
listen_port = 2345

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((listen_ip, listen_port))

#vorodi 1-5 migire


while True:
    print("Listening on {}:{}".format(listen_ip, listen_port))
    request, addr=server.recvfrom(4096)
    print("Recived: {} from {}:{}".format(request,addr[0], addr[1]))
    server.sendto("ack!!", addr)