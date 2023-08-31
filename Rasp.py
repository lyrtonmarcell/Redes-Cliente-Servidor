#Received IP: ['E20000172211009418905449', 'E2000017221101321890548C', 'E2000017221101241890547C', 'E20000172211010218905459', 'E20000172211011118905471', 'E20000172211012518905484', 'E2000017221100961890544A', 'E20000172211011718905474', 'E20000172211010118905454']
#!/usr/bin/env python3
import mercury
import sys 
from datetime import datetime
import socket
import json
param = 2300

if len(sys.argv) > 1:
        param = int(sys.argv[1])

# configura a leitura na porta serial onde esta o sensor
reader = mercury.Reader("tmr:///dev/ttyUSB0")

# para funcionar use sempre a regiao "NA2" (Americas)
reader.set_region("NA2")

# nao altere a potencia do sinal para nao prejudicar a placa
reader.set_read_plan([1], "GEN2", read_power=param)

# realiza a leitura das TAGs proximas e imprime na tela
# print(reader.read())
tag_string = []
epcs = map(lambda tag: tag, reader.read())
for tag in epcs:
    print(tag.epc, tag.read_count, tag.rssi, datetime.fromtimestamp(tag.timestamp))
    tag_string.append(tag.epc.decode('utf-8'))

#tag_string = ''
#tag_string = tag.epc.decode('utf-8')
# Cria um socket para a comunicao com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conecta-se ao endereço IP e porta do servidor
client_socket.connect(('172.16.103.8', 8080))

# Prepara o corpo da solicitação POST em formato JSON
request_body = json.dumps({'ip': tag_string})
# Cria a requisição POST com os cabeçalhos necessários
request = f"POST /add_ip HTTP/1.1\r\nHost: 172.16.103.8:8080\r\nContent-Length: {len(request_body)}\r\nContent-Type: application/json\r\n\r\n{request_body}"
# Envia a requisição para o servidor
client_socket.send(request.encode('utf-8'))
# Recebe a resposta do servidor
response = client_socket.recv(1024)
# Exibe a resposta decodificada
print(response.decode('utf-8'))
# Fecha conexão
client_socket.close()
