import json
import socket
from mfrc522 import SimpleMFRC522
import requests

def read_rfid():
    reader = SimpleMFRC522()
    print("Aproxime uma tag RFID")
    try:
        id, _ = reader.read()
        return str(id)
    finally:
        GPIO.cleanup()

def send_rfid_to_server(rfid):
    server_address = 'IP_DO_SERVIDOR'
    server_port = 8080

    payload = {'rfid': rfid}
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(f'http://{server_address}:{server_port}/add_rfid', json=payload, headers=headers)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Erro ao enviar RFID para o servidor:", e)

if __name__ == '__main__':
    while True:
        rfid = read_rfid()
        print("RFID Tag:", rfid)
        send_rfid_to_server(rfid)
