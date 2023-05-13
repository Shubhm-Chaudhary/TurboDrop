import socket


def send_file(file_path, ip, port):
    print("Sending File")
    # Create a socket object
    s = socket.socket()

    # Connect to the server
    s.connect((ip, port))

    # Open the file in binary mode
    with open(file_path, "rb") as f:
        # Read the file data
        file_data = f.read()

        # Send the file data
        s.sendall(file_data)

    # Close the socket connection
    s.close()


def receive_file(file_path, port):
    # Create a socket object
    s = socket.socket()

    # Bind the socket to a port
    s.bind(("0.0.0.0", port))

    # Listen for incoming connections
    s.listen()

    # Accept a connection
    conn, addr = s.accept()

    # Open the file in binary mode
    with open(file_path, "wb") as f:
        # Receive the file data
        file_data = conn.recv(1024)
        while file_data:
            f.write(file_data)
            file_data = conn.recv(1024)

    # Close the connection and socket
    conn.close()
    s.close()


# Send a file
send_file(r"C:\Users\shubh\Downloads\python-3.8.0-amd64.exe", "192.108.493.605", 8000)
print("File Sent")

# Receive a file
# receive_file("received_file.exe", 8000)
