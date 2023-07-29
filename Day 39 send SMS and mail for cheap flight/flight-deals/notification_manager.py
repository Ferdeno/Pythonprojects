from twilio.rest import Client
import smtplib

TWILIO_SID = "AC6bc98690e6ce8d74525292f427bf3556"
TWILIO_AUTH_TOKEN = "f90941f509f87728d0d5cd7e34bccfee"
TWILIO_VIRTUAL_NUMBER = "+15416973044"
TWILIO_VERIFIED_NUMBER = "+919677749649"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) :
      self.client=Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
      self.email="t72053126@gmail.com"
      self.password="sxihhfqnxzojinkg"
        
    def send_sms(self,message):
        
        send_message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(send_message.status)

    def send_email(self,message,email):
      with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=self.email,password=self.password)
        for e in email:
          connection.sendmail(
              from_addr=self.email,
              to_addrs=e,
              msg=f"Subject : Flight Ticket Alert!!! \n\n {message}".encode('utf-8'))
