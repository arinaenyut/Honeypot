#!/usr/bin/env python

import argparse
import socket
import logging

logging.basicConfig(filename='logfile.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

def connection_handling(client, addr):
	client_ip = addr[0]
	logging.info('Connection from {}'.format(client_ip))
	print('Connection: from {}'.format(client_ip))
	

def start_server(port, bind):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#объект сокета с агрументами - семейтсва адресов и тип сокета
    sock.bind((bind, port))

    #сервер-приманка чтобы открыть порт и связать с приложением
    while True:
        sock.listen(100)
        print('Listening for connection on port {} ...'.format(port))
        client, addr = sock.accept()
        #обработка подключения
        connection_handling(client, addr)
        
    client.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run an SSH honeypot server')#обработка аргументов командной строки
    parser.add_argument("--port", "-p", help="The port to bind the ssh server to (default 22)", default=8080, type=int, action="store")#фргументы
    parser.add_argument("--bind", "-b", help="The address to bind the ssh server to", default="", type=str, action="store")#pirt,bind
    args = parser.parse_args()#в переменной аргументы
    start_server(args.port, args.bind)
