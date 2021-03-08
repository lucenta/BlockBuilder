import socket
import threading
import json

CLIENTS = {} # Maintain dict of clients. Each client has a queue, and a lock.
lock = threading.Lock()

def add_to_clients_queue(location):
	for q in CLIENTS:
		CLIENTS[q].append(location)

# Function (Thread) to process the queue for a user
def process_queue(c,addr):
	ID = (c,addr)
	while True:
		if len(CLIENTS[ID]) != 0:
			location = CLIENTS[ID].pop(0)
			c.sendall(location.encode('utf-8'))


# Function (Thread) to handle when user adds a block
def addBlock_handler(clientsocket,addr):
	print("Client joined with",addr)
	while True:
		msg = clientsocket.recv(1024).decode('utf-8')
		if not msg:
			break
		# print(msg)
		# print(msg,"from",addr)
		add_to_clients_queue(msg) # Add new block placement to client queues
	print("Client",addr,"disconnected")
	clientsocket.close()

def main():
	s = socket.socket()
	host = '0.0.0.0'
	port = 9001
	print("Started, waiting for clients...")
	s.bind((host,port))
	s.listen(5)

	while True:
		c, addr = s.accept()
		CLIENTS[(c,addr)] = [] # Add a queue and lock for the client
		a = threading.Thread(target=addBlock_handler, args=(c,addr)) # Create thread to handle adding block from client
		p = threading.Thread(target=process_queue, args=(c,addr))
		a.start()
		p.start()
	s.close()

main()