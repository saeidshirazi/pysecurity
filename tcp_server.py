import socket
import  threading


#0.0.0.0 yani hame ip haye system
listen_ip = '0.0.0.0'
listen_port = 2345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((listen_ip, listen_port))

#vorodi 1-5 migire

server.listen(5)

def handle_client(client):

    request = client.recv(4096)
    print("Revieved : {}".format(request))
    client.send("ACK!")
    client.close()

while True:
    print("Listening on {}:{}".format(listen_ip, listen_port))
    client_socket, addr = server.accept()
    print("Connetction accepted from {}:{}".format(addr[0], addr[1]))
    client_handler=threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
