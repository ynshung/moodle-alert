import requests
from inspect import cleandoc

def send_telegram(message, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID):
    telegram_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": cleandoc(message),
        "parse_mode": "MarkdownV2",
    }
    response = requests.post(telegram_url, data=data)
    if response.status_code == 200:
        print(f"Message sent successfully: {message}")
    else:
        print(f"Failed to send message: {message}")
        print(response.text)
