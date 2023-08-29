import socket
import json

def send_post_request(ip):
    # Cria um socket para a comunicação com o servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta-se ao endereço IP e porta do servidor
    client_socket.connect(('172.16.103.8', 8080))

    # Prepara o corpo da solicitação POST em formato JSON
    request_body = json.dumps({'ip': ip})
    # Cria a requisição POST com os cabeçalhos necessários
    request = f"POST /add_ip HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nContent-Length: {len(request_body)}\r\nContent-Type: application/json\r\n\r\n{request_body}"
    # Envia a requisição para o servidor
    client_socket.send(request.encode('utf-8'))
    # Recebe a resposta do servidor
    response = client_socket.recv(1024)
    # Exibe a resposta decodificada
    print(response.decode('utf-8'))
    # Fecha conexão
    client_socket.close()

def send_put_request(ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.16.103.8', 8080))

    request_body = json.dumps({'ip': ip})
    request = f"PUT /update_ip HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nContent-Length: {len(request_body)}\r\nContent-Type: application/json\r\n\r\n{request_body}"
    client_socket.send(request.encode('utf-8'))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))
    client_socket.close()

def send_patch_request(ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.16.103.8', 8080))

    request_body = json.dumps({'ip': ip})
    request = f"PATCH /patch_ip HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nContent-Length: {len(request_body)}\r\nContent-Type: application/json\r\n\r\n{request_body}"
    client_socket.send(request.encode('utf-8'))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))
    client_socket.close()

def send_delete_request(ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('172.16.103.8', 8080))

    request_body = json.dumps({'ip': ip})
    request = f"DELETE /delete_ip HTTP/1.1\r\nHost: 127.0.0.1:8080\r\nContent-Length: {len(request_body)}\r\nContent-Type: application/json\r\n\r\n{request_body}"
    client_socket.send(request.encode('utf-8'))
    response = client_socket.recv(1024)
    print(response.decode('utf-8'))
    client_socket.close()

def send_get_request():
    # Cria um socket para a comunicação com o servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta-se ao endereço IP e porta do servidor
    client_socket.connect(('172.16.103.8', 8080))
    # Cria a requisição GET com os cabeçalhos necessários
    request = "GET /get_ips HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n\r\n"
    # Envia a requisição para o servidor
    client_socket.send(request.encode('utf-8'))

    # Inicializa uma variável para armazenar a resposta do servidor
    response_data = b""
    # Loop para receber os dados da resposta em blocos de 1024 bytes
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response_data += data

    # Separa o cabeçalho da resposta dos dados JSON
    response_json = json.loads(response_data.split(b'\r\n\r\n')[1].decode('utf-8'))
    # Obtém a lista de IPs do JSON da resposta
    ips = response_json.get('ips')
    if ips:
        print("Lista de IPs:")
        for ip in ips:
            print(ip)
    else:
        print("Não tem IPs cadastrados.")

    client_socket.close()

if __name__ == '__main__':
    while True:
        action = input("Escolha uma das opções (post/get/exit): ").lower()
        if action == 'exit':
            break
        if action == 'post':
            ip = input("Adicione um IP: ")
            send_post_request(ip)
        if action == 'get':
            send_get_request()
