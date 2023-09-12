#Received IP: ['E20000172211009418905449', 'E2000017221101321890548C', 'E2000017221101241890547C', 'E20000172211010218905459', 'E20000172211011118905471', 'E20000172211012518905484', 'E2000017221100961890544A', 'E20000172211011718905474', 'E20000172211010118905454']
#!/usr/bin/env python3
import http.server
import socketserver
import json
import mercury
from datetime import datetime
import threading
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/itens':
            # Realiza a leitura das tags ao receber uma solicitação GET para /itens
            tag_string = read_tags()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'itens': tag_string}).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

def read_tags():
    #tag_string=['E20000172211009418905449', 'E2000017221101321890548C', 'E2000017221101241890547C', 'E20000172211010218905459', 'E20000172211011118905471', 'E20000172211012518905484', 'E2000017221100961890544A', 'E20000172211011718905474', 'E20000172211010118905454']

    
    param = 2300
    # configura a leitura na porta serial onde está o sensor
    reader = mercury.Reader("tmr:///dev/ttyUSB0")

    # para funcionar use sempre a região "NA2" (Americas)
    reader.set_region("NA2")

    # não altere a potência do sinal para não prejudicar a placa
    reader.set_read_plan([1], "GEN2", read_power=param)

    # realiza a leitura das TAGs próximas e imprime na tela
    tag_string = []
    epcs = map(lambda tag: tag, reader.read())
    for tag in epcs:
        print(tag.epc, tag.read_count, tag.rssi, datetime.fromtimestamp(tag.timestamp))
        tag_string.append(tag.epc.decode('utf-8'))
    return tag_string

def main():
    port = 4000
    with socketserver.ThreadingTCPServer(('127.0.0.1', port), RequestHandler) as httpd:
        print(f'Servidor escutando na porta {port}...')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    main()

