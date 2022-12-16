import argparse
import socket

MAX_SIZE = 65535

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 3000
    host = '127.0.0.1'
    s.bind((host, port))
    s.listen(1)
    print('Server is running on', s.getsockname())
    while True:
        sc, clientAddress = s.accept()
        print('Client connected from', clientAddress)
        # recvall needs to be implemented
        data = sc.recv(MAX_SIZE)
        message = data.decode('ascii')
        print('Client >> ', message)
        if(message == 'exit'):
            break
        reply = input('Server >> ')
        sc.sendall(reply.encode('ascii'))
    sc.close()

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    s.connect(('127.0.0.1', 3000))
    while True:
        message = input('Client >> ')
        data = message.encode('ascii')
        s.sendall(data)
        if(message == 'exit'):
            break
        # recvall needs to be implemented
        reply = s.recv(MAX_SIZE)
        print('Server >> ', reply.decode('ascii'))
    s.close()
    

if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    # parser.add_argument('-p', metavar='PORT', type=int, default=3000,
    # help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    # function(args.p)
    function()
