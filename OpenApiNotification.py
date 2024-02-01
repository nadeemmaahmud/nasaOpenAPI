import requests
import json
from pync import Notifier
import time

def display_notification(dicts):
    dict_data = json.dumps(dicts, indent = 0)

    notification_title = "Notification From Nadim"
    notification_message = f"Message : {dict_data}"

    try:
        Notifier.notify(
            title = notification_title,
            message = notification_message,
            timeout = 10
        )
    except Exception as e:
        print(f"Error displaying notification: {e}")

if __name__ == "__main__":
    api_url = "https://www.boredapi.com/api/activity?participants=1"
    res = requests.get(api_url)

    content = res.content.decode("UTF-8")
    dict_content = json.loads(content)
    display_notification(dict_content)
    time.sleep(15)