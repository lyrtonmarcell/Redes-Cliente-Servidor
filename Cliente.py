import http.client
import json
import socket
import random

def send_post_request(host, path, payload):
    headers = {"Content-Type": "application/json"}
    payload_json = json.dumps(payload)
    conn = http.client.HTTPConnection(host)
    conn.request("POST", path, body=payload_json, headers=headers)
    response = conn.getresponse()
    data = response.read().decode()
    conn.close()
    return response.status, data

def send_tags_to_server(host, path, nome_caixa, tags):
    payload = {"nome_caixa": nome_caixa, "tags": tags}
    status, response = send_post_request(host, path, payload)
    if status == 200:
        print(f"Tags enviadas com sucesso para o servidor para o caixa '{nome_caixa}'.")
    else:
        print(f"Falha ao enviar as tags para o servidor para o caixa '{nome_caixa}'. Status: {status}, Resposta: {response}")


def generate_unique_ip():
    # Gerar um IP aleatório dentro da faixa 192.168.1.x
    ip = f"192.168.1.{random.randint(1, 255)}"
    return ip

def get_stock_from_server(host, path):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read().decode()
    conn.close()
    return json.loads(data)

def main():
    host = "127.0.0.1:3000"  # Endereço do servidor RESTful
    unique_ip = generate_unique_ip()
    caixa_name = f"caixa{unique_ip.replace('.', '')}"
    print(f"Nome da caixa gerado: {caixa_name}")

    payload = {"nome": caixa_name, "endereco": unique_ip, "status": "aberto"}
    status, response = send_post_request(host, "/registrar", payload)
    if status == 200:
        print(f"Nome da caixa ({caixa_name}), endereço IP ({unique_ip}) e status 'aberto' enviados com sucesso para o servidor.")
    else:
        print(f"Falha ao enviar os dados para o servidor. Status: {status}, Resposta: {response}")

    while True:
        user_input = input("Pressione 'S' para enviar tags ou 'Q' para sair: ").strip().lower()
        
        if user_input == 's':
            tags = [
                'E20000172211009418905449',
                'E20000172211009418905449',
                'E2000017221101321890548C',
                'E2000017221101321890548C',
                'E2000017221101241890547C',
                'E20000172211010218905459',
                'E20000172211011118905471',
                'E20000172211012518905484',
                'E2000017221100961890544A',
                'E20000172211011718905474',
                'E20000172211010118905454'
            ]
            send_tags_to_server(host, "/armazenar_tags", caixa_name, tags)
            stock = get_stock_from_server(host, "/estoque")
            print("Produtos armazenados:")
            
            # Contagem de produtos com base no número de tags iguais
            product_count = {}
            for tag in tags:
                if tag in stock:
                    product_name = stock[tag]['nome']
                    product_price = stock[tag]['preco']
                    if product_name not in product_count:
                        product_count[product_name] = {'preco': product_price, 'quantidade': 1}
                    else:
                        product_count[product_name]['quantidade'] += 1
                        product_price=product_price*product_count[product_name]['quantidade']

            total_price = 0
            for product_name, product_info in product_count.items():
                print(f"Nome do Produto: {product_name}, Preço: {product_info['preco']}, Quantidade: {product_info['quantidade']}")
                total_price += product_info['preco'] * product_info['quantidade']

            print(f"Preço Total: {total_price}")
        elif user_input == 'q':
            break
        else:
            print("Comando inválido. Pressione 'S' para enviar tags ou 'Q' para sair.")

if __name__ == "__main__":
    main()
