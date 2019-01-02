from twilio.rest import Client

accoundSID = 'ACc4ff7bc2bd74e730585937949d202bbc'
authToken = '7bff467ef9f3ca89f75081518d1590d2'

client = Client(accoundSID, authToken)
myTwilioNumber = '+17254659871'
myCellPhone = input('Enter number:\n')
myBodyMessage = input('Enter message:\n')
message = client.messages.create(
                                from_=myTwilioNumber, 
                                body=myBodyMessage, 
                                to='+1' + myCellPhone
                            )
print(message.sid)