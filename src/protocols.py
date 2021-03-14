import socket
import json

'''
This file contains the protocol used to send and receive actions. 
Each message is delimited by the DELIMITER
'''
DELIMITER = b'$'

# Encode an action, encode it, add delimiter, then send it
def send_action(action,s):
	j = json.dumps(action).encode('utf-8')+DELIMITER
	s.send(j)


# Recieve an action 1 byte at a time until we reach our delimiter
def recv_action(s):
	action=b''
	while True:
		part = s.recv(1)
		if not part:
			return ''
		if part == DELIMITER:
			break
		action+=part
	return json.loads(action.decode('utf-8'))
