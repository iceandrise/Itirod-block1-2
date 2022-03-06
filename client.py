import threading
import socket

nickname = input("Enter your name: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 33333))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break

def write():
    idd = 0
    while True:
        idd+=1
        message = f'[{idd}]{nickname} : {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()

        
  