import socket
import time

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket.gethostbyname(socket.gethostname()))
# Bind the socket to a specific address and port
server_address = ('34.16.160.152', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    connection, client_address = server_socket.accept()

    try:
        print('Connection from', client_address)

        # Receive the data
        while True:
            data = connection.recv(16)

            print('Received {!r}'.format(data))

            data = data.decode()
            print(data)
            dosya = open("tahmin_verileri.txt", "r")
            gun = int(dosya.readline())
            while 1:
                satir = dosya.readline()
                if (data in satir):
                    satir = satir.split(",")
                    del satir[0]
                    satir.insert(5+gun,"t")
                    connection.sendall(str(satir).encode())
                    print(satir)
                    dosya.close()
                    break


            break


    finally:
        # Clean up the connection
        connection.close()
