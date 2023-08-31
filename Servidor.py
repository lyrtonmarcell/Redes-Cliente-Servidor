import socket
import threading
import json

# Lista para armazenar os IPs
ips = []
# Lock para sincronização em acesso concorrente à lista de IPs
ips_lock = threading.Lock()
# Dicionário para armazenar as informações dos clientes
clients_info = {}
# Lock para sincronização em acesso concorrente ao dicionário de informações dos clientes
clients_info_lock = threading.Lock()
def handle_client(client_socket):
    # Recebe os dados da requisição do cliente
    request_data = client_socket.recv(1024)
    # Converte os dados recebidos para texto (string)
    request_text = request_data.decode('utf-8')


    # Verifica se a requisição é do tipo GET /get_clients
    if "GET /get_clients" in request_text:
    # Bloqueia o acesso ao dicionário de informações dos clientes enquanto é lido
        with clients_info_lock:
            # Converte o dicionário de informações dos clientes em JSON e codifica em bytes
            response_data =json.dumps(clients_info).encode('utf-8')
            # Monta a resposta com o cabeçalho apropriado
            response = "HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}".format(len(response_data), response_data.decode('utf-8'))

# Verifica se a requisição é do tipo POST /add_client
    if "POST /add_client" in request_text:
        # Encontra o tamanho do corpo da requisição
        content_length_start = request_text.find("Content-Length: ") + len("Content-Length: ")
        content_length_end = request_text.find("\r\n", content_length_start)
        content_length = int(request_text[content_length_start:content_length_end])

        # Extrai o corpo da requisição
        request_body = request_text.split("\r\n\r\n")[1]
        # Converte o corpo da requisição JSON em um dicionário
        request_json = json.loads(request_body)

        # Obtém o IP do cliente
        client_ip = client_socket.getpeername()[0]

        # Obtém informações do cliente do dicionário
        client_status = request_json.get('status')

        if client_status is not None:
            # Bloqueia o acesso ao dicionário de informações dos clientes enquanto é modificado
            with clients_info_lock:
                # Adiciona informações do cliente ao dicionário
                clients_info[client_ip] = {'status': client_status}
                print(f"Added client: {client_ip} with status: {client_status}")
                response = "HTTP/1.1 200 OK\r\n\r\nClient addition successful"
        else:
            response = "HTTP/1.1 400 Bad Request\r\n\r\nMissing or invalid client information"


    # Verifica se a requisição é do tipo GET /get_ips
    if "GET /get_ips" in request_text:
        # Bloqueia o acesso à lista de IPs enquanto é lida
        with ips_lock:
            # Converte a lista de IPs em um JSON e codifica em bytes
            response_data =json.dumps({'ips': ips}).encode('utf-8')
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
# Função para iniciar o servidor
def start_server():
    # Cria um socket para o servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Liga o socket ao endereço IP e porta
    server_socket.bind(('127.0.0.1', 8080))
    # Inicia a escuta por conexões
    server_socket.listen(10)
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
