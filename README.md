# 🎉 Holiday Bot (Slack + GitHub Actions)

This project automates **holiday reminders** for Slack using **GitHub Actions**.  
It checks an Excel file (`holidays.xlsx`) daily, and if tomorrow is a holiday, it posts a message to your Slack channel(s).  
It also creates a **GitHub Issue reminder** every year on Jan 1st, reminding you to update the holiday list.

## ⚙️ Setup Instructions

### 1. Slack Setup
1. Create a Slack App → add **Bot Token (xoxb-...)**
2. Give it permission: `chat:write`
3. Install it in your workspace
4. Invite it to your target channel(s). Paste below command to the channel you want to invite.  
/invite @HolidayBot

### 2. GitHub Secrets
Go to: **Repo → Settings → Secrets and variables → Actions → New repository secret**  
Add:
- `SLACK_BOT_TOKEN` → your Slack bot token (`xoxb-...`)
- `SLACK_CHANNEL_IDS` → comma-separated Slack channel IDs (e.g., `C01ABCD123,C02XYZ456`)

 ### 3. Excel File
Maintain your holidays in `holidays.xlsx` with headers:

| date(d/m/y) | festival      | location  |
|-------------|--------------|------------|
| 05/09/2025  | Onam         | Chennai    |
| 24/12/2025  | Christmas    | World      |
| 26/01/2026  | Republic Day | India      |

Message format is auto-generated:  
Tomorrow {date} on the occasion of {festival} is a holiday for {location} location. 🎉

## ⏰ Scheduling

- **Daily Slack job** (`holiday.yml`) runs at **6:45 PM IST** (→ `13:15 UTC` in cron).
- **Annual reminder job** (`reminder.yml`) runs every **Jan 1st at 09:00 UTC**, creating an issue to update `holidays.xlsx`.

You can also **manually run both workflows** from the GitHub **Actions** tab.
 
