import os
from datetime import date, timedelta
from slack_sdk import WebClient
from holidays import FESTIVALS

# Load Slack Bot token from GitHub Actions secrets
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_ID = os.getenv("SLACK_CHANNEL_ID").split(",")  # e.g. "C12345,C67890"  # set in GitHub secrets

client = WebClient(token=SLACK_BOT_TOKEN)

def check_and_send():
    today = date.today()
    tomorrow = today + timedelta(days=1)

    if tomorrow in FESTIVALS:
        message = FESTIVALS[tomorrow]
        client.chat_postMessage(channel=CHANNEL_ID, text=message)
        print(f"✅ Sent: {message}")
    else:
        print("ℹ️ No holiday tomorrow.")

if __name__ == "__main__":
    check_and_send()

