#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
import socket
import threading
from threading import Thread


def read_sok():
    while True:
        data = sor.recv(1024)
        print(f'{dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}: server read mes from {alias}: {data.decode("utf-8")}')


def send_sok():
    if message:
        sor.sendto(('[' + alias + ']: ' + message).encode('utf-8'), server)
        print(f'{dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}: {alias} send mes to server: {message}')


server = '127.0.0.1', 9090  # Данные сервера
alias = 'client'  # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('127.0.0.1', 0))  # Задаем сокет как клиент
sor.sendto((alias + ' connect to server').encode('utf-8'), server)  # Уведомляем сервер о подключении
message = None
handler_read: Thread = threading.Thread(target=read_sok)
handler_read.start()
handler_send: Thread = threading.Thread(target=send_sok)
handler_send.start()
while True:
    message = input()
    send_sok()