from twilio.rest import Client

# Your Twilio account credentials
account_sid = 'AC3b86ed0167906fc3a81b8a4b59eb11a7'
auth_token = '7e4fb80cf2d0fb58fc03bf8cb9b6b391'

# Create a Twilio client
client = Client(account_sid, auth_token)
call = client.calls.create(
    twiml='<Response><Say>Hello I am pluto from dipanjan, gud marani gandu bahanchod</Say></Response>',
    from_='+14067977522',  # Your Twilio phone number
    to='+918327233024'  # Destination phone number
)

print('Call initiated. Call SID:', call.sid)
