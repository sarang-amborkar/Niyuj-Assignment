# client.py

import socket                   # Import socket module
from cryptography.fernet import Fernet


def decrypt():
    fkey =  "yfe3iB66MOQThoGk1rQc6KKPEkTpjVJaWfvWMXnLjqo="
    # key = fkey.read()
    cipher = Fernet(fkey)

    with open('encrypted_file','rb') as df:
        encrypted_data = df.read()

    decrypted_file = cipher.decrypt(encrypted_data)

    with open('received_file.txt','wb') as df:
        df.write(decrypted_file)


def receive_file():
    s = socket.socket()             # Create a socket object
    host = socket.gethostname()     # Get local machine name
    port = 60000                    # Reserve a port for your service.

    s.connect((host, port))
    s.send(b"Hello server!")

    with open('encrypted_file', 'wb') as f:
        print('file opened')
        while True:
            print('receiving data...')
            data = s.recv(1024)
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')
    s.close()
    print('connection closed')


if __name__ == "__main__":
    receive_file()
    decrypt()