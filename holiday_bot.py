import os
from datetime import date, timedelta
from slack_sdk import WebClient
from holidays import FESTIVALS

# Load your Slack Bot token (set as environment variable)
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
client = WebClient(token=SLACK_BOT_TOKEN)

# Replace with your channel ID (e.g. C12345…)
CHANNEL_ID = "C09DV2XTG9W"

def check_and_send():
    today = date.today()
    tomorrow = today + timedelta(days=1)

    if tomorrow in FESTIVALS:
        message = FESTIVALS[tomorrow]
        client.chat_postMessage(channel=CHANNEL_ID, text=message)
        print(f"✅ Sent: {message}")

if __name__ == "__main__":
    check_and_send()


