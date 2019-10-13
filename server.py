#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime as dt
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while True:
    data, address_client = sock.recvfrom(1024)
    print(address_client[0], address_client[1])
    print(f'{dt.datetime.today().strftime("%Y-%m-%d %H:%M:%S")}: get mes: {data.decode("utf-8")}')
    if address_client not in client:
        client.append(address_client)  # Если клиента нету , то добавить
    for clients in client:
        #       if clients == address_client:
        #          continue  # Не отправлять данные клиенту который их прислал
        sock.sendto(data, clients)   # Отправить уведомление о приеме сообщения
