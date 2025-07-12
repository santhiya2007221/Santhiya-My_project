from plyer import notification

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name="Desktop Notifier",
        app_icon=None,  # Change this to the path of your icon if you want
        timeout=10
    )

# Example usage:
notify("Hello", "This is a desktop notification!")
