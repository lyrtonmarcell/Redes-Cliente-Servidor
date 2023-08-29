import socket
import threading
import json

# Lista para armazenar os IPs
ips = []
# Lock para sincronização em acesso concorrente à lista de IPs
ips_lock = threading.Lock()

def handle_client(client_socket):
    # Recebe os dados da requisição do cliente
    request_data = client_socket.recv(1024)
    # Converte os dados recebidos para texto (string)
    request_text = request_data.decode('utf-8')

    # Verifica se a requisição é do tipo GET /get_ips
    if "GET /get_ips" in request_text:
        # Bloqueia o acesso à lista de IPs enquanto é lida
        with ips_lock:
            # Converte a lista de IPs em um JSON e codifica em bytes
            response_data = json.dumps({'ips': ips}).encode('utf-8')
            # Monta a resposta com o cabeçalho apropriado
            response = "HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}".format(len(response_data), response_data.decode('utf-8'))
    # Verifica se a requisição é do tipo POST /add_ip
    if "POST /add_ip" in request_text:
        # Encontra o tamanho do corpo da requisição
        content_length_start = request_text.find("Content-Length: ") + len("Content-Length: ")
        content_length_end = request_text.find("\r\n", content_length_start)
        content_length = int(request_text[content_length_start:content_length_end])

        # Extrai o corpo da requisição
        request_body = request_text.split("\r\n\r\n")[1]
        # Converte o corpo da requisição JSON em um dicionário
        request_json = json.loads(request_body)

        # Obtém o IP do dicionário
        ip = request_json.get('ip')
        if ip:
            # Bloqueia o acesso à lista de IPs enquanto é modificada
            with ips_lock:
                ips.append(ip)
                print(f"Received IP: {ip}")
                response = "HTTP/1.1 200 OK\r\n\r\nIP addition successful"
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nMissing or invalid IP"
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"
      
    # Envia a resposta para o cliente
    client_socket.send(response.encode('utf-8'))
    client_socket.close()

    # Verifica se a requisição é do tipo PUT /update_ip
    if "PUT /update_ip" in request_text:
        # Encontra o tamanho do corpo da requisição
        content_length_start = request_text.find("Content-Length: ") + len("Content-Length: ")
        content_length_end = request_text.find("\r\n", content_length_start)
        content_length = int(request_text[content_length_start:content_length_end])
    
        # Extrai o corpo da requisição
        request_body = request_text.split("\r\n\r\n")[1]
        # Converte o corpo da requisição JSON em um dicionário
        request_json = json.loads(request_body)
    
        # Obtém o IP do dicionário
        ip = request_json.get('ip')
        if ip:
            # Bloqueia o acesso à lista de IPs enquanto é modificada
            with ips_lock:
                if ip in ips:
                    # Atualiza o IP existente
                    print(f"Updating IP: {ip}")
                    response = "HTTP/1.1 200 OK\r\n\r\nIP update successful"
                else:
                    response = "HTTP/1.1 404 Not Found\r\n\r\nIP not found"
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nMissing or invalid IP"
    
    # Verifica se a requisição é do tipo PATCH /patch_ip
    if "PATCH /patch_ip" in request_text:
        # Encontra o tamanho do corpo da requisição
        content_length_start = request_text.find("Content-Length: ") + len("Content-Length: ")
        content_length_end = request_text.find("\r\n", content_length_start)
        content_length = int(request_text[content_length_start:content_length_end])
    
        # Extrai o corpo da requisição
        request_body = request_text.split("\r\n\r\n")[1]
        # Converte o corpo da requisição JSON em um dicionário
        request_json = json.loads(request_body)
    
        # Obtém o IP do dicionário
        ip = request_json.get('ip')
        if ip:
            # Bloqueia o acesso à lista de IPs enquanto é modificada
            with ips_lock:
                if ip in ips:
                    # Aplica as atualizações parciais no IP existente
                    print(f"Patching IP: {ip}")
                    response = "HTTP/1.1 200 OK\r\n\r\nIP patch successful"
                else:
                    response = "HTTP/1.1 404 Not Found\r\n\r\nIP not found"
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nMissing or invalid IP"
    
    # Verifica se a requisição é do tipo DELETE /delete_ip
    elif "DELETE /delete_ip" in request_text:
        # Encontra o tamanho do corpo da requisição
        content_length_start = request_text.find("Content-Length: ") + len("Content-Length: ")
        content_length_end = request_text.find("\r\n", content_length_start)
        content_length = int(request_text[content_length_start:content_length_end])
    
        # Extrai o corpo da requisição
        request_body = request_text.split("\r\n\r\n")[1]
        # Converte o corpo da requisição JSON em um dicionário
        request_json = json.loads(request_body)
    
        # Obtém o IP do dicionário
        ip = request_json.get('ip')
        if ip:
            # Bloqueia o acesso à lista de IPs enquanto é modificada
            with ips_lock:
                if ip in ips:
                    # Remove o IP da lista
                    ips.remove(ip)
                    print(f"Deleted IP: {ip}")
                    response = "HTTP/1.1 200 OK\r\n\r\nIP deletion successful"
                else:
                    response = "HTTP/1.1 404 Not Found\r\n\r\nIP not found"
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nMissing or invalid IP"

# Função para iniciar o servidor
def start_server():
    # Cria um socket para o servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Liga o socket ao endereço IP e porta
    server_socket.bind(('172.16.103.8', 8080))
    # Inicia a escuta por conexões
    server_socket.listen(5)
    # Exibe uma mensagem de que o servidor está ouvindo
    print("Servidor ouvindo na porta 8080")

    # Loop para aceitar e lidar com as conexões dos clientes
    while True:
        # Aceita uma conexão e obtém o socket do cliente e o endereço
        client_socket, addr = server_socket.accept()
        # Cria uma thread para lidar com o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        # Inicia a thread
        client_thread.start()
      
# Inicia o servidor quando este arquivo é executado diretamente
if __name__ == '__main__':
    start_server()

