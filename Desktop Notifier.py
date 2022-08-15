import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Title here..........",
            message = "Message here.....",
            timeout = 10
        )
        time.sleep(3600)
