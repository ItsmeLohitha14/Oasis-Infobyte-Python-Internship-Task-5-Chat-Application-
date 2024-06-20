import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        # Receive message from the client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        # Print the received message
        print(f"[{client_address}] {message}")

        # Echo the message back to the client
        client_socket.send(message.encode('utf-8'))

    # Close connection with the client
    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Main function to set up the server
def main():
    # Server configuration
    host = '127.0.0.1'  # localhost
    port = 12345  # Choose any free port you like

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen()

    print(f"[LISTENING] Server is listening on {host}:{port}...")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()

        # Start a new thread to handle client communication
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Run the server
if __name__ == "__main__":
    main()
