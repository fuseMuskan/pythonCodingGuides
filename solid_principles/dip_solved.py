from abc import ABC, abstractmethod

class EmailSender:
    def send_email(self, recipient, subject, message):
        # Code to send an email
        print(f"Sending email to {recipient}: {subject} - {message}")



class NotificationService:
    def __init__(self, email_source):
        self.email_source = email_source  # Depends on abstraction, not implementation class

    def send_notification(self, recipient, message):
        self.email_source.get_email(recipient, message)



class EmailSource(ABC):
    @abstractmethod
    def get_email(self, recipient, message):
        pass


class EmailSourceImplementation(EmailSource):  # Concrete implementation of EmailSource
    def __init__(self):
        self.email_sender = EmailSender()

    def get_email(self, recipient, message):
        self.email_sender.send_email(recipient, "Notification", message)



# Using the NotificationService to send a notification
email_source = EmailSourceImplementation()
notification_service = NotificationService(email_source)
notification_service.send_notification("user@example.com", "Hello, this is a notification!")
