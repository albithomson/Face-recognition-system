from twilio.rest import Client
import keys


def sms():
    client = Client(keys.account_sid,keys.auth_token)

    message = client.messages.create(
        body="Hello your son is present in class",
        from_=keys.twilio_number,
        to=keys.my_phone_number
        )
    print(message.body)