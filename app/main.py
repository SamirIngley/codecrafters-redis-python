import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")


    with socket.create_server(("localhost", 6379), reuse_port=True) as server_socket: # starts listening for client requests 
        conn, _ = server_socket.accept() # blocks exectution until client sends data

        while True: 
            data = conn.recv(1024)
            if not data: 
                break
            conn.sendall(b"+PONG\r\n")
        

    print("Connection Data: ", conn)

    conn.sendall(b"+PONG\r\n")



if __name__ == "__main__":
    main()
