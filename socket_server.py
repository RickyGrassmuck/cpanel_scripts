#!/usr/bin/python
from __future__ import print_function
import socket
import sys
import getopt
from thread import *


def clientthread(conn, port):
    hostname = socket.gethostname()

    conn.send('Connected to {host} on port {port} Type something and hit enter\n'.format(host=hostname, port=port))

    while True:
        data = conn.recv(1024)
        reply = 'OK... {}'.format(data)
        if not data:
            break

        conn.sendall(reply)

    conn.close()


def main(argv):
    host = ''
    port = ''

    try:
        opts, args = getopt.getopt(argv, "hp:", ["port="])
    except getopt.GetoptError:
        print('test.py -p <PORT>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -p <PORT>')
            sys.exit()

        elif opt in ("-p", "--port"):

            if isinstance(int(arg), (int, long)):
                port = int(arg)

        else:
            print("Port argument must be an integer")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')

    try:
        s.bind((host, port))
    except socket.error as msg:
        print('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        sys.exit()

    print('Socket bind complete')

    s.listen(10)
    print('Socket now listening on port ' + str(port))

    while 1:
        conn, addr = s.accept()
        print('Connected with ' + addr[0] + ':' + str(addr[1]))

        start_new_thread(clientthread, (conn, str(port),))
        s.close()


if __name__ == "__main__":
    main(sys.argv[1:])
