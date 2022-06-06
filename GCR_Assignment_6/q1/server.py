import socket


def createSocket():
    s = socket.socket()
    host = "127.0.0.1"
    port = 3000

    s.bind((host, port))

    return s


def waitForConnections():
    print("Server started on port 3000")
    print("Waiting for connection...")
    s = createSocket()
    s.listen(5)

    listen = True

    while listen:
        conn, addr = s.accept()
        print(f"Connection started from {addr}")
        conn.send("ls && pwd".encode("utf-8"))
        conn.close()
        break


if __name__ == "__main__":
    waitForConnections()
