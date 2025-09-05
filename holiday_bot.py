import os
from datetime import date, timedelta
from slack_sdk import WebClient
from holidays import FESTIVALS

# Load Slack Bot token from GitHub Secrets
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")

# Load multiple channel IDs (comma-separated) from GitHub Secrets
# Example: "C12345,C67890,C13579"
CHANNEL_IDS = os.getenv("SLACK_CHANNEL_IDS", "").split(",")

client = WebClient(token=SLACK_BOT_TOKEN)

def check_and_send():
    today = date.today()
    tomorrow = today + timedelta(days=1)

    if tomorrow in FESTIVALS:
        message = FESTIVALS[tomorrow]
        for channel in CHANNEL_IDS:
            channel_id = channel.strip()
            if channel_id:  # ensure it's not empty
                try:
                    client.chat_postMessage(channel=channel_id, text=message)
                    print(f"✅ Sent to channel {channel_id}: {message}")
                except Exception as e:
                    print(f"❌ Failed to send to {channel_id}: {e}")
    else:
        print("ℹ️ No holiday tomorrow.")

if __name__ == "__main__":
    check_and_send()
