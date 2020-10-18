from forex_python.converter import CurrencyRates
from twilio.rest import Client
import requests

SID = 'SID_from_twilio_here'
auth_key='AUTH_key_From Twilio
from_no = 'number_by_twilio'
to_no ='Ur_registered_number'
print ("Flag 1")
c = CurrencyRates()
//You can change the line below to your prefered exchange
response = c.get_rate('USD','INR')
print ("USD to INR exchange rate : "+str(response))

client = Client(SID,auth_key)
message = client.messages.create(
            body = "USD to INR exchange rate is : "+str(response),
            from_ =from_no,
            to = to_no
          )

print (message.sid)
print (message.status)
