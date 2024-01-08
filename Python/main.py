import socket

# Replace 'localhost' with the actual IP address or hostname of your Node.js server
HOST = 'localhost'
PORT = 3000

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server
    s.connect((HOST, PORT))

    while True:
        # Take user input
        user_input = input("Enter a message to send to the server (type 'exit' to close): ")

        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            break

        # Send user input to the server
        s.sendall(user_input.encode('utf-8'))

        # Receive and print the response from the server
        data = s.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
