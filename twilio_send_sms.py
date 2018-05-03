from twilio.rest import Client

# Your Account SID from https://www.twilio.com/try-twilio
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from https://www.twilio.com/try-twilio
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)

# Fill in Message Fields
message = "Hi Jenny! This is to confirm your reservation."
to_phone_number = "+15558675309"
# from number must be your Twilio phone number, found on your Twilio account page
from_phone_number = "+15017250604"

# Send message 
message = client.messages.create(
    to=to_phone_number,
    from_= from_phone_number,
    body= message)

print(message.sid)
