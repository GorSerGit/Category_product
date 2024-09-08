import socket
import json
from main import main

# Создаем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Определяем адрес и порт
server_address = ('localhost', 8888)

# Привязываем сокет к адресу и порту
server_socket.bind(server_address)

# Слушаем за подключениями
server_socket.listen(1)

print("Сервер запущен...")

while True:
    # Принимаем подключение
    client_socket, client_address = server_socket.accept()
    
    try:
        # Получаем данные от клиента
        data = client_socket.recv(4096)
        
        data = data.decode('utf-8')
        print(f"Получено сообщение от клиента: {data}")

        # Обрабатываем данные
        response = str(main(data))
        
        # Отправляем ответ клиенту
        client_socket.sendall(response.encode())
        
    finally:
        # Закрываем соединение
        client_socket.close()


