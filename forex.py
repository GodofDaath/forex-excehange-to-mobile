from forex_python.converter import CurrencyRates
from twilio.rest import Client
import requests


SID = 'AC5a9312e981d44381ca74fd4271d6dbae'
auth_key='a89730dbffe4edd02374cb36c0d7facc'
from_no = '+18723956098'
to_no ='+918897620121'
print ("Flag 1")
c = CurrencyRates()
print ("Flag 2")
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
