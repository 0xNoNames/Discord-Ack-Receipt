import socket
from datetime import datetime

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080
IMAGE_PATH = "1x1.png"
IMAGE_SIZE = 124

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print("You can now send http://%s:%s/jean to Jean and know when he opens your message!\n" % (SERVER_HOST, SERVER_PORT))

while True:
    client_socket, client_address = server_socket.accept()

    request = client_socket.recv(1024).decode().split("\n")
    informations = {"ip" : client_address[0], "date" : datetime.now().strftime('%d-%m-%Y %H:%M:%S UTC'), "username" : "", "useragent" : ""}
    for line in request:
        if ("GET /" in line.upper()): 
            informations["username"] = " ".join(line.split()[1][1:].split())
        elif ("USER-AGENT" in line.upper()):
            informations["useragent"] = " ".join(line.split(":", 1)[1].split())
            break

    print("[%s] - %s(%s) - %s" % (informations["date"], informations["username"], informations["ip"], informations["useragent"]))

    response = "HTTP/1.1 200 OK\nContent-Type: image/png\nContent-Length: %s\n\n" % IMAGE_SIZE
    client_socket.sendall(response.encode())
    
    with open(IMAGE_PATH, "rb") as img:
        client_socket.sendall(img.read())

    client_socket.close()

server_socket.close()