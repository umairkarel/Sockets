""" 
    Developed on Oct 10, 2021

    author: @umairkarel
"""

import socket

HEADER = 64  # every msg will be of 64 byte (len)
PORT = 5050  # TCP port
SERVER = "192.168.0.118"
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = "utf-8"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    """
    Sends a message over a TCP socket connection.

    Args:
        msg (str): The message to be sent.

    Returns:
        None

    Raises:
        None

    Note:
        The function assumes that the client socket connection has already
        been established and stored in the `client` variable.

    """
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # Converting to 64 length
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
# input()
send("Hello Everyone!")
# input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)
