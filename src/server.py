import socket
import threading


def client_handler(clientsocket,addr):
	print("Client joined with",clientsocket,addr)
	while True:
		msg = clientsocket.recv(1024).decode()
		if not msg:
			break
		print(msg,"from",addr)
		#Send message back to user
	print("Client",clientsocket,addr,"disconnected")
	clientsocket.close()


s = socket.socket()
host = socket.gethostname()
port = 9000
print("Started, waiting for clients...")
s.bind((host,port))
s.listen(5)

while True:
	c, addr = s.accept()
	print("WE GOT ONE")
	t=threading.Thread(target=client_handler, args=(c,addr))
	t.start()




s.close()