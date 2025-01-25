Description of the Program :
The program's primary goal is to create a Python bot that reminds users of pending tasks using desktop notifications and Telegram messages. Below is a breakdown of its components and functionality:

:Purpose
-The bot aims to improve task management by:
-Sending timely desktop notifications to remind users of their tasks.
-Delivering Telegram messages to a specified chat for added convenience and accessibility.

1. Task Management:  
   - Add, delete, and list pending tasks.  
   - Set deadlines for tasks.  

2. Notification System:  
   - Desktop Notifications: Use libraries like plyer or win10toast to display reminders on the user's screen.  
   - Telegram Integration: Use the Telegram Bot API (python-telegram-bot library) to send reminders as messages.  

Key Components:
  Libraries and Their Roles
-time: Manages timing by introducing delays between notifications, ensuring tasks are reminded in intervals.
-plyer.notification: Allows the program to send desktop notifications, displaying task details directly on the user's screen.
-telegram.Bot: Enables interaction with Telegram's API to send messages to a specified user or group chat using a bot.

Configuration:
 Telegram Bot Token (TOKEN):
-A unique key to authenticate the bot and allow access to the Telegram Bot API.
-It is required to send messages programmatically.
 Chat ID (CHAT_ID):
-Identifies the recipient chat or user for message delivery.
-This is needed to direct reminders to the correct Telegram user or group.

Tasks:
A predefined list of tasks serves as the source of reminders. Each task is processed sequentially to ensure reminders are sent one at a time.
Reminder Logic

The bot iterates over the task list and sends both:
-A desktop notification using the plyer library.
-A Telegram message using the python-telegram-bot library.
-After each reminder, the bot waits for 1 minute (time.sleep(60)) before processing the next task.

Structure Explanation:
Dependencies:

import time: This module provides time-related functions. In our case, we use it to introduce delays between task reminders.

from plyer import notification: Plyer is a library for accessing features commonly found on mobile devices in a platform-neutral way. We use it to send desktop notifications.

from telegram import Bot: This module allows us to interact with the Telegram API to send messages. We use it to send task reminders via Telegram.

Task Management:

tasks = ["Complete project report" "Attend team meeting", "Submit timesheet"]: This is a simple list to store the pending tasks. You can modify this list to include any tasks you want to be reminded of.
Reminder Function:

remind_tasks(): This function iterates over the list of tasks and calls both send_desktop_notification and send_telegram_message functions to send reminders. It introduces a delay of 60 seconds between each reminder using the time.sleep(60) function.
