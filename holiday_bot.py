import os
import csv
from datetime import datetime, date, timedelta
from slack_sdk import WebClient

SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
CHANNEL_IDS = os.getenv("SLACK_CHANNEL_IDS", "").split(",")

client = WebClient(token=SLACK_BOT_TOKEN)

def load_festivals():
    festivals = {}
    with open("holidays.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Parse dd/mm/yyyy format
            holiday_date = datetime.strptime(row["date(d/m/y)"], "%d/%m/%Y").date()
            festivals[holiday_date] = {
                "festival": row["festival"],
                "location": row["location"]
            }
    return festivals

def check_and_send():
    festivals = load_festivals()
    today = date.today()
    tomorrow = today + timedelta(days=1)
    print(f"📅 Today: {today}, Tomorrow: {tomorrow}")

    if tomorrow in festivals:
        details = festivals[tomorrow]
        message = (
            f"Tomorrow {tomorrow.strftime('%d-%B-%Y')} "
            f"on the occasion of {details['festival']} "
            f"is a holiday for {details['location']} location. 🎉"
        )
        for channel in CHANNEL_IDS:
            channel_id = channel.strip()
            if channel_id:
                try:
                    client.chat_postMessage(channel=channel_id, text=message)
                    print(f"✅ Sent to {channel_id}: {message}")
                except Exception as e:
                    print(f"❌ Failed to send to {channel_id}: {e}")
    else:
        print("ℹ️ No holiday tomorrow.")

if __name__ == "__main__":
    check_and_send()

