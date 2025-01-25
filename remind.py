import time
from plyer import notification
from telegram import Bot

# Telegram bot token and chat ID
TOKEN = '7370067932:AAGRbUapxZWKwADoXjsSLXxHSqyOG4gTsNg'
CHAT_ID = '5670032536'

# List of pending tasks
tasks = ["Complete project report", "Attend team meeting", "Submit timesheet"]

# Function to send desktop notification
def send_desktop_notification(task):
    notification.notify(
        title='Task Reminder',
        message=task,
        timeout=10
    )

# Function to send Telegram message
def send_telegram_message(task):
    bot = Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=f"Reminder: {task}")

# Function to remind users of pending tasks
def remind_tasks():
    for task in tasks:
        send_desktop_notification(task)
        send_telegram_message(task)
        # Wait 1 minute before sending the next reminder
        time.sleep(60)

if _name_ == '_main_':
    remind_tasks()
