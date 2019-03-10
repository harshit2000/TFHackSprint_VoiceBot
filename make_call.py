# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC7152ef78e137c43c5eae98361482be0d'
auth_token = 'ad53384dd5792428cdc5f55850829489'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+919582705290',
                        from_='+13088324954'
                    )

print(call.sid)
