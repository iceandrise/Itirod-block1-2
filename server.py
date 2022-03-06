import threading
import socket

host = '127.0.0.1'
port = 33333

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(2)

clients = []
nicknames = []


def broadcast(message):
    for client in clients:
        client.send(message)
        

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            client.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    count = 0
    idd = 0 
    while True:
        idd += 1
        count += 1
        if(count<=3):
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii') )
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            print(f'Client nickname {nickname}')
            broadcast(f'{nickname} join the chat!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target = handle, args = (client,))
            thread.start()
        else:
            print("Socket closed")
            broadcast(f'{nickname} Socket closed!'.encode('ascii'))
            count-=1

print("Server listening...")
receive()