import socket

# Function to handle sending and receiving messages
def start_client():
    # Client configuration
    host = '127.0.0.1'  # localhost
    port = 12345  # The same port as used by the server

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    print("[CONNECTED] You are connected to the chat server.")

    while True:
        # Send message to the server
        message = input("Enter your message: ")
        client_socket.send(message.encode('utf-8'))

        # Receive echo from the server
        echo_message = client_socket.recv(1024).decode('utf-8')
        print(f"Server echoed: {echo_message}")

    # Close the connection
    client_socket.close()

# Run the client
if __name__ == "__main__":
    start_client()
