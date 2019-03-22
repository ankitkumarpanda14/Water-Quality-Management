import requests

class messenger:  
    TWILIO_SID = 'ACd51c35ce54dce5ec56df1da9ce74582d'
    TWILIO_AUTHTOKEN = '0134a0c8d980002b045bc52be908f21d'
    TWILIO_MESSAGE_ENDPOINT = 'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json'.format(TWILIO_SID=TWILIO_SID)
    TWILIO_NUMBER = 'whatsapp:+14155238886'

    def __init__(self,message):
        self.msg_wa = message

##    def send_whatsapp_message(self,to, message):
##        message_data = {
##            "To": to,
##            "From": TWILIO_NUMBER,
##            "Body": message,
##        }
##        response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
##        
##        response_json = response.json()
##        
##        
##        return response_json

    def message_maker(self):
        TWILIO_SID = 'ACd51c35ce54dce5ec56df1da9ce74582d'
        TWILIO_AUTHTOKEN = '0134a0c8d980002b045bc52be908f21d'
        TWILIO_MESSAGE_ENDPOINT = 'https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json'.format(TWILIO_SID=TWILIO_SID)
        TWILIO_NUMBER = 'whatsapp:+14155238886'
        to_number = 'whatsapp:+919861169611' 
##        self.appointment_msg = self.msg_wa
##        msg = send_whatsapp_message(to_number, self.appointment_msg)
        message_data = {
            "To": to_number,
            "From": TWILIO_NUMBER,
            "Body": self.msg_wa,
        }
        response = requests.post(TWILIO_MESSAGE_ENDPOINT, data=message_data, auth=(TWILIO_SID, TWILIO_AUTHTOKEN))
        
        response_json = response.json()
 
        print("Message Sent") # SM5xxxafa561e34b1e84c9d22351ae08a0

