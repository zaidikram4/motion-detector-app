import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD = "lzlpzdwepenqisvk"
SENDER = "applesamsung532@gmail.com"
RECEIVER = "applesamsung532@gmail.com"

def send_email(image_path):
    print("Email Started")
    email_message = EmailMessage()
    email_message["Subject"] = ("Motion Detected!")
    email_message.set_content("Movement has been detected")
    print("Email Ended")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == "__main__":
    send_email(image_path=f"images/{image_with_object}.png")
