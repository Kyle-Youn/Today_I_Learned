

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 'port기재(숫자 자료형)')

message = '메세지 기재'
print(f"send message: {message}")

sock.sendto(message.encode('utf-8'), server_address)