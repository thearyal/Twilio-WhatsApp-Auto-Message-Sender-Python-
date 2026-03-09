from twilio.rest import Client
from datetime import datetime
import time

# Your Twilio credentials
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)


def get_user_input():
    """Get input from user"""
    to_number = input("Enter receiver number (with +countrycode): ")
    message_body = input("Enter your message: ")
    hour = int(input("Enter hour (24 format): "))
    minute = int(input("Enter minute: "))
    
    return to_number, message_body, hour, minute


def wait_until_time(hour, minute):
    """Wait until the scheduled time"""
    now = datetime.now()
    target_time = now.replace(hour=hour, minute=minute, second=0)

    if target_time < now:
        print("Time already passed today ❌")
        return False

    wait_seconds = (target_time - now).total_seconds()
    print(f"Message will send in {int(wait_seconds)} seconds...")
    
    time.sleep(wait_seconds)
    return True


def send_whatsapp_message(to_number, message_body):
    """Send WhatsApp message using Twilio"""
    message = client.messages.create(
        from_='whatsapp:+141552365466',
        body=message_body,
        to=f'whatsapp:{to_number}'
    )

    print("Message Sent Successfully")
    print("Message SID:", message.sid)


def main():
    print("=== Twilio WhatsApp Auto Sender ===")
    
    to_number, message_body, hour, minute = get_user_input()
    
    if wait_until_time(hour, minute):
        send_whatsapp_message(to_number, message_body)


if __name__ == "__main__":
    main()