# server.py

import socket                   # Import socket module
from cryptography.fernet import Fernet


def encrypt():
    fkey = "yfe3iB66MOQThoGk1rQc6KKPEkTpjVJaWfvWMXnLjqo="
    # key = fkey.read()
    cipher = Fernet(fkey)

    filename = 'test.txt'

    with open(filename, 'rb') as f:
        e_file = f.read()

    encrypted_file = cipher.encrypt(e_file)

    with open(filename + "encrypted", 'wb') as ef:
        ef.write(encrypted_file)


def send_file():
    port = 60000                    # Reserve a port for your service.
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    s.bind((host, port))            # Bind to the port
    s.listen(5)                     # Now wait for client connection.

    print('Server listening....')

    while True:
        conn, addr = s.accept()     # Establish connection with client.
        print('Got connection from', addr)
        data = conn.recv(1024)
        print('Server received', repr(data))

        filename='test.txtencrypted'
        f = open(filename,'rb')
        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()


if __name__ == "__main__":
    encrypt()
    send_file()

