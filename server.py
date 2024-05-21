""" 
    Developed on Oct 10, 2021

    author: @umairkarel
"""

import socket
import threading

HEADER = 64  # every msg will be of 64 byte (len)
PORT = 5050  # TCP port
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

# SOCK_STREAM -> TCP (Transmission Control Protocol) -> connection based socket (Exchange msg)
# SOCK_DGRAM  -> UDP (User Datagram Protocol) -> No Exchange based.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    """
    Handles a client connection.

    Args:
        conn (socket.socket): The client socket connection.
        addr (tuple): The client address.

    Returns:
        None

    Raises:
        None
    """
    print("[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # Blocking line
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg Recieved!".encode(FORMAT))


def start():
    """
    Starts the server and listens for incoming connections.

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # conn -> socket obj that allows to communicate back
        # adrr -> info about connection
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.enumerate() - 1}")


print("[STARTING] Server is starting....")
start()
