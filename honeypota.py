#!/usr/bin/env python

import argparse
import socket
import logging
import threading
import paramiko

logging.basicConfig(filename='logfile.log', format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
host_key = paramiko.RSAKey(filename = 'server.key') #ключ хоста

class SSH_Honeypot(paramiko.ServerInterface):

	def __init__(self, client_ip): 	
		self.event = threading.Event()
		self.client_ip = client_ip 
		
	#запрос канала	
	def check_channel_request(self,kind,chanid):
		logging.info('Check channel request ({}) - {}'.format(self.client_ip, kind))
		if kind == 'session':
			return paramiko.OPEN_SUCCEEDED
			
	#допуск любого пароля при аутентификации		
	def check_auth_password(self,username,password):
		logging.info('ATTEMPT TO LOGIN ({}) - username: {} - password: {}'.format(self.client_ip, username, password))
		return paramiko.AUTH_SUCCESSFUL
	
	#возвращает список методов аутентификации
	def get_allowed_auths(self, username):	
		logging.info('Authentication allowed ({}) - {}'.format(self.client_ip, username))
		return 'publickey,password'
	
	#допуск ключа клиента c паролем	
	def check_auth_publickey(username, key):
		return paramiko.AUTH_SUCCESSFUL
        	
        #доступ к shell	
	def check_channel_shell_request(self, channel):
		return True

	#доступ к псевдотерминалу
	def check_channel_pty_request(self, c, t, w, h, p, ph, m):
		return True
	
   
def connection_handling(client, addr):
	client_ip = addr[0]
	logging.info('Connection from {}'.format(client_ip))
	print('Connection: from {}'.format(client_ip))	
	
	#создание транспортного объекта
	t = paramiko.Transport(client)
	t.add_server_key(host_key)  #добавить ключ хоста
	server = SSH_Honeypot(client_ip) 
	t.start_server(server=server) #запустить сервер

	
def start_server(port, bind):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#объект сокета с агрументами - семейтсва адресов и тип сокета
    
    sock.bind((bind, port))

    #сервер-приманка чтобы открыть порт и связать с приложением
    while True:
        sock.listen(100)
        print('Listening for connection on port {} ...'.format(port))
        client, addr = sock.accept()
        #обработка подключения
        new_client = connection_handling(client, addr)
        
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run an SSH honeypot server')#обработка аргументов командной строки
    parser.add_argument("--port", "-p", help="The port to bind the ssh server to (default 22)", default=8080, type=int, action="store")#фргументы
    parser.add_argument("--bind", "-b", help="The address to bind the ssh server to", default="", type=str, action="store")#pirt,bind
    args = parser.parse_args()#в переменной аргументы
    start_server(args.port, args.bind)
