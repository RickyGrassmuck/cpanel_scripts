#!/usr/bin/python

import socket
import sys, getopt
from thread import *

#Function for handling connections. This will be used to create threads
def clientthread(conn, port):
    HOSTNAME = socket.gethostname()

    #Sending message to connected client
    conn.send('Connected to ' + HOSTNAME + ' on port ' + port + '. Type something and hit enter\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()

def main(argv):
	HOST = ''   # Symbolic name meaning all available interfaces
	PORT = '' # Arbitrary non-privileged port

	try:
	  opts, args = getopt.getopt(argv,"hp:",["port="])
	except getopt.GetoptError:
	  print 'test.py -p <PORT>'
	  sys.exit(2)
	for opt, arg in opts:
	  if opt == '-h':
		 print 'test.py -p <PORT>'
		 sys.exit()
	  elif opt in ("-p", "--port"):
		 if isinstance(int(arg), (int, long)):
			PORT = int(arg)
		 else:
			print "Port argument must be an integer"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print 'Socket created'

	#Bind socket to local host and port
	try:
		s.bind((HOST, PORT))
	except socket.error as msg:
		print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
		sys.exit()

	print 'Socket bind complete'

	#Start listening on socket
	s.listen(10)
	print 'Socket now listening on port ' + str(PORT)
	
	#now keep talking with the client
	while 1:
		#wait to accept a connection - blocking call
		conn, addr = s.accept()
		print 'Connected with ' + addr[0] + ':' + str(addr[1])

		#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
		start_new_thread(clientthread ,(conn, str(PORT),))
        s.close()
		

if __name__ == "__main__":
   main(sys.argv[1:])
