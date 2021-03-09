import socket
import threading
import json
import protocols as p

CLIENTS = {} # Maintain dict of clients. Each client has a queue, and a lock.
lock = threading.Lock()

# Broadcast an action to all clients except for the one who sent it
def broadcast(action,c,addr):
	# Since the number of CLIENTS can be modified, we must lock the resource incase we delete one while iterating
	ID = (c,addr)
	lock.acquire()
	for q in CLIENTS:
		if q != ID:
			CLIENTS[q].append(action)
	lock.release()

# Function (Thread) to process the queue for a user
def process_queue(c,addr):
	ID = (c,addr)
	try:
		while True:
			if len(CLIENTS[ID]) != 0:
				location = CLIENTS[ID].pop(0)
				p.send_action(location,c)
				# c.sendall(location.encode('utf-8'))
	except KeyError:
		return # End the thread if we get a key error, meaning the client has been removed from the dict


# Function (Thread) to handle when client sends action to server
def addBlock_handler(c,addr):
	print("Client joined with",addr)
	while True:
		# msg = c.recv(1024).decode('utf-8')
		action = p.recv_action(c)
		print(action)
		if not action:
			break
		# print(msg)
		# print(msg,"from",addr)
		broadcast(action,c,addr) # Add new block placement to client queues
	disconnect_client(c,addr)


# Remove client from CLIENTS dict if they diconnect, also close their connection
def disconnect_client(c,addr):
	print("Client",addr,"disconnected")
	lock.acquire()
	del CLIENTS[(c,addr)]
	lock.release()
	c.close()

'''
Two threads are created for each client that connects. One thread handles the actions that the client sends to the server
(i.e. adding or removing a block). When a user performs an action, the action is sent to the queue associated with that client
The second thread processes the queue.

This functionality is chosen to ensure that things run smooothly and we don't block our receives with sends, or vice versa.
'''
def main():
	s = socket.socket()
	host = '0.0.0.0'
	port = 9000
	print("Started, waiting for clients...")
	s.bind((host,port))
	s.listen(5)

	while True:
		c, addr = s.accept()
		CLIENTS[(c,addr)] = [] # Add a queue and lock for the client
		a = threading.Thread(target=addBlock_handler, args=(c,addr)) # Create thread to handle adding block from client
		p = threading.Thread(target=process_queue, args=(c,addr))	# Create a thread to process the queue for a client
		a.start()
		p.start()
	s.close()

main()