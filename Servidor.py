import http.server
import socketserver
import json

# Dicionário para armazenar informações das caixas
caixas = {}

# Dicionário para armazenar as tags
tags_dict = {}

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/caixas':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(caixas).encode())
        elif self.path == '/tags':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(tags_dict).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_PUT(self):
        if self.path.startswith('/caixas/'):
            caixa = self.path.split('/')[-1]
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                payload = self.rfile.read(content_length)
                data = json.loads(payload.decode())
                if 'status' in data:
                    # Atualizar o status da caixa se ela existir
                    if caixa in caixas:
                        caixas[caixa]['status'] = data['status']
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(json.dumps({'message': 'Status da caixa atualizado com sucesso.'}).encode())
                    else:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write(json.dumps({'error': f'Caixa "{caixa}" não encontrada.'}).encode())
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Solicitação PUT inválida.'}).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Solicitação PUT inválida. Sem corpo de mensagem.'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def do_POST(self):
        if self.path == '/registrar':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                payload = self.rfile.read(content_length)
                data = json.loads(payload.decode())
                if 'nome' in data and 'endereco' in data and 'status' in data:
                    nome = data['nome']
                    endereco = data['endereco']
                    status = data['status']
                    # Adicionar a nova entrada ao dicionário de caixas
                    caixas[nome] = {'endereco': endereco, 'status': status}
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(json.dumps({'message': 'Caixa registrada com sucesso.'}).encode())
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Solicitação POST inválida.'}).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Solicitação POST inválida. Sem corpo de mensagem.'}).encode())
        elif self.path == '/armazenar_tags':
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length > 0:
                payload = self.rfile.read(content_length)
                data = json.loads(payload.decode())
                if 'nome_caixa' in data and 'tags' in data:
                    nome_caixa = data['nome_caixa']
                    tags = data['tags']
                    # Verificar o status da caixa
                    if nome_caixa in caixas:
                        if caixas[nome_caixa]['status'] == 'bloqueado':
                            self.send_response(400)
                            self.end_headers()
                            self.wfile.write(json.dumps({'error': f'A caixa "{nome_caixa}" está bloqueada.'}).encode())
                            return
                        # Adicionar as tags ao dicionário de tags usando o nome_caixa como chave
                        tags_dict[nome_caixa] = tags
                        self.send_response(200)
                        self.end_headers()
                        self.wfile.write(json.dumps({'message': f'Tags armazenadas com sucesso para a caixa "{nome_caixa}".'}).encode())
                    else:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write(json.dumps({'error': f'Caixa "{nome_caixa}" não encontrada.'}).encode())
                else:
                    self.send_response(400)
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': 'Solicitação POST inválida. Deve incluir "nome_caixa" e "tags".'}).encode())
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Solicitação POST inválida. Sem corpo de mensagem.'}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def main():
    port = 3000
    with socketserver.TCPServer(('127.0.0.1', port), RequestHandler) as httpd:
        print(f'Servidor escutando na porta {port}...')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()
        client_thread.start()

# Inicia o servidor quando este arquivo é executado diretamente
if __name__ == '__main__':
    start_server()
