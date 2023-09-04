import http.client
import json

def send_get_request(host, path):
    conn = http.client.HTTPConnection(host)
    conn.request("GET", path)
    response = conn.getresponse()
    data = response.read().decode()
    conn.close()
    return response.status, data

def send_put_request(host, path, payload):
    headers = {"Content-Type": "application/json"}
    payload_json = json.dumps(payload)
    conn = http.client.HTTPConnection(host)
    conn.request("PUT", path, body=payload_json, headers=headers)
    response = conn.getresponse()
    data = response.read().decode()
    conn.close()
    return response.status, data

def main():
    host = "127.0.0.1:3000"  # Endereço do servidor RESTful

    while True:
        print("Escolha uma opção:")
        print("1. Ver informações das caixas (GET)")
        print("2. Modificar informações de uma caixa (PUT)")
        print("3. Ver informações dos históricos de compras (GET)")
        print("4. Ver estoque (GET)")
        print("5. Sair")
        choice = input("Opção: ")

        if choice == "1":
            status, response = send_get_request(host, "/caixas")
            if status == 200:
                caixas = json.loads(response)
                for nome_caixa, detalhes_caixa in caixas.items():
                    print(f"Nome: {nome_caixa}, Endereço: {detalhes_caixa['endereco']}, Status: {detalhes_caixa['status']}")
            else:
                print("Falha ao obter informações das caixas.")
        elif choice == "2":
            caixa = input("Digite o nome da caixa: ")
            status = input("Digite o novo status (Aberto ou Bloqueado): ")
            payload = {"status": status}
            status, response = send_put_request(host, f"/caixas/{caixa}", payload)
            if status == 200:
                print(json.loads(response)["message"])
            else:
                print("Falha ao atualizar o status da caixa.")
        elif choice == "3":
            status, response = send_get_request(host, "/tags")
            if status == 200:
                tags = json.loads(response)
                formatted_tags = json.dumps(tags, indent=2)
                print(formatted_tags)
            else:
                print("Falha ao obter informações de tags.")
        elif choice == "4":
            status, response = send_get_request(host, "/estoque")
            if status == 200:
                estoque = json.loads(response)
                formatted_estoque = json.dumps(estoque, indent=2)
                print(formatted_estoque)
            else:
                print("Falha ao obter informações de estoque.")
        elif choice == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
