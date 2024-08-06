import socket

# 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 주소 바인딩
server_socket.bind(('localhost', 12345))

# 연결 요청 대기
server_socket.listen(1)

# 클라이언트 연결 수락
connection, client_address = server_socket.accept()

print(f"Connected by {client_address}")

# 클라이언트로부터 데이터 수신
data = connection.recv(1024)  # 1024 바이트까지 데이터를 받을 수 있음

# 데이터가 있을 경우 디코딩
if data:
    message = data.decode('utf-8')
    print(f"Received message: {message}")

# 연결 종료
connection.close()
server_socket.close()
