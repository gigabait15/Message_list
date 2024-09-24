import asyncio
import json
from channels.generic.websocket import WebsocketConsumer

from EmailMessage.utils import EmailAc

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def receive(self, text_data):
        data = json.loads(text_data)
        email_name = data.get('email')

        ec = EmailAc(email_name)
        mails = asyncio.run(ec.len_mail())
        total_count = len(mails)

        self.send(json.dumps({'total': total_count}))

        for i in mails[::-1]:
            self.send(json.dumps({'message': asyncio.run(ec.mail_info(i))}))



