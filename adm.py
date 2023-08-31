import socket
import json
def get_clients():
# Cria um socket para a comunicação com o servidor
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta-se ao endereço IP e porta do servidor
    client_socket.connect(('127.0.0.1', 8080))
    # Cria a requisição GET com os cabeçalhos necessários
    request = "GET /get_clients HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n\r\n"
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
    ips_clientes = response_json.get('client_ip')
    if ips:
        print("Lista de IPs dos clientes:")
        for cliente_ip in ips:
            print(cliente_ip)
    else:
        print("Não tem IPs cadastrados.")

    client_socket.close()

def update_client_status(client_ip, new_status):
    payload = {'status': new_status}
    response = requests.put(f'{server_address}/update_status/{client_ip}', json=payload)
    if response.status_code == 200:
        print(f'Successfully updated status for {client_ip}')
    else:
        print(f'Failed to update status for {client_ip}')

if __name__ == '__main__':
    while True:
        print("1. Get Clients")
        print("2. Update Client Status")
        choice = input("Enter your choice: ")

        if choice == '1':
            clients = get_clients()
            print("Connected Clients:")
            for client_ip, client_info in clients.items():
                print(f"IP: {client_ip}, Status: {client_info['status']}")

        elif choice == '2':
            client_ip = input("Enter client IP: ")
            new_status = input("Enter new status (true/false): ")
            update_client_status(client_ip, new_status)

        else:
            print("Invalid choice")
