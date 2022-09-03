from slack_sdk.webhook import WebhookClient
from src.config import config

def send_text_message(text):
    webhook = WebhookClient(config.SLACK_WEBHOOK_URL)
    webhook.send(
        text=text
    )