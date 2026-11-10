import socket  # noqa: F401
from concurrent.futures import ThreadPoolExecutor

'''
Some learnings about Sockets/Connections
One listening socket listens for client requests, opens 
a new socket + connection for each client/request
'''

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    with ThreadPoolExecutor(max_workers=4) as executor: # blocks rest of fn until threads within block complete
        while True: 
            conn, _ = server_socket.accept() # accepts new clients - opens a connection, or blocks execution until client sends request
            executor.submit(client_handler, conn) 
        
def client_handler(conn_in): 
    # receives requests for one client
    while data := conn_in.recv(1024): # if no request, will block execution until data contains data or close connection
        if not data: 
            break
        conn_in.sendall(b"+PONG\r\n")

if __name__ == "__main__":
    main()
