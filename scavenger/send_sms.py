
# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os 

account_sid = 'AC54450e35c4ac9014a109a3b3f34ac0fb'
auth_token = 'd5f2f183ce43b89a1ffeba11906c0d81'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+19314633580',
         to='+17193222610'
     )

print(message.sid)