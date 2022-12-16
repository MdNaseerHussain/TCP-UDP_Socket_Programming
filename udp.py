import argparse
import socket

MAX_SIZE_BYTES = 65535

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    port = 3000
    host = '127.0.0.1'
    s.bind((host, port))
    print('Server is running on', s.getsockname())
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print('Client >> ', message)
        if(message == 'exit'):
            break
        reply = input('Server >> ')
        s.sendto(reply.encode('ascii'), clientAddress)

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        message = input('Client >> ')
        data = message.encode('ascii')
        s.sendto(data, ('127.0.0.1', 3000))
        if(message == 'exit'):
            break
        reply, serverAddress = s.recvfrom(MAX_SIZE_BYTES)
        print('Server >> ', reply.decode('ascii'))

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
