import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 2882))
serversocket.listen(5)
#Serve the faggots
while True:
    (clientsocket, (ip, port)) = serversocket.accept()
    ipinfo = "Connected adress: " + ip + "\n"
    chunks = []
    bytes_recd = 0
    ipinfo = ipinfo + clientsocket.recv(2048).decode('utf-8')
    f = open(ip + "-announce.txt", "w")
    f.write(ipinfo)
    f.close()
    clientsocket.close()


