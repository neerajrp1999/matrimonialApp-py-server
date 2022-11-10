import firebase_admin
from firebase_admin import credentials, messaging
d="D:/Neeraj/FCM-with-Python-and-Android-master/key.json"
k="matrimonial-app-android-firebase.json"
cred = credentials.Certificate(k)

firebase_admin.initialize_app(cred)

def sendPush(title, msg, registration_token, dataObject=None):
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )
    
    response = messaging.send_multicast(message)
    print('Successfully sent message:', response)


def send_to_token():
    # [START send_to_token]
    # This registration token comes from the client FCM SDKs.
    registration_token = 'YOUR_REGISTRATION_TOKEN'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data={
            'score': '850',
            'time': '2:45',
        },
        token=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)
    # [END send_to_token]