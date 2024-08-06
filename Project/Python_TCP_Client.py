import socket

def tcp_client():
    # 서버 주소와 포트 설정
    server_address = ('localhost', 12345)
    
    # 소켓 생성
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 서버에 연결
        client_socket.connect(server_address)
        print("Connected to server at", server_address)
        
        # 서버로 메시지 전송
        message = "Hello, server!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent message: {message}")
        
        # 서버로부터 응답 받기
        response = client_socket.recv(1024)  # 최대 1024 바이트를 수신
        print("Received response:", response.decode('utf-8'))
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # 소켓 닫기
        client_socket.close()
        print("Connection closed.")

if __name__ == '__main__':
    tcp_client()
