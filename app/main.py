import socket  # noqa: F401
from concurrent.futures import ThreadPoolExecutor

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    conn, _ = server_socket.accept() # blocks execution until client sends request

    while data := conn.recv(1024): # if no request, data will simply block execution until data found or close connection found
        if not data: 
            break
        with ThreadPoolExecutor(max_workers=4)  as executor: 
            response_thread = executor.submit(respond(conn, data)) 
            
        result = response_thread.result()
        print(result)
        
    print("Connection Data: ", conn)

def respond(conn, data_in): 
    conn.sendall(b"+PONG\r\n")

if __name__ == "__main__":
    main()
