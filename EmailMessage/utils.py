import email
import imaplib
from email.header import decode_header
import dotenv
from datetime import datetime
from EmailMessage.models import EmailAccount


dotenv.load_dotenv()


class EmailAc:
    def __init__(self, email_name):
        self.username = email_name
        self.email_data = EmailAccount.objects.get(email=self.username)
        self.password = self.email_data.password
        self.provider = self.email_data.provider
        self.imap = None

    async def connect(self):
        if self.imap is None:
            self.imap = imaplib.IMAP4_SSL(f'imap.{self.provider}')
            self.imap.login(self.username, self.password)
            self.imap.select("INBOX")

    async def len_mail(self):
        await self.connect()
        status, messages = self.imap.search(None, 'ALL')
        return messages[0].split() if messages[0] else []

    async def mail(self, num_mail):
        status, msg_data = self.imap.fetch(num_mail, '(RFC822)')
        msg = email.message_from_bytes(msg_data[0][1])
        return msg

    async def subject(self, num):
        msg = await self.mail(num)
        for part in msg.walk():
            if part.get_content_maintype() == 'text' and part.get_content_subtype() == 'plain':
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset()
                if charset:
                    try:
                        return payload.decode(charset)
                    except Exception as e:
                        print(f"Ошибка декодирования: {e}")
                        return payload.decode('utf-8', errors='replace')

        return "Без сообщения"

    async def mail_info(self, num):
        msg = await self.mail(num)
        letter_date = email.utils.parsedate_tz(msg["Date"])
        info = {
            'letter_date': datetime(*letter_date[:6]).strftime('%Y-%m-%d %H:%M:%S'),
            'letter_id': msg["Message-ID"],
            'letter_from': msg["Return-path"],
            'letter_title': decode_header(msg["Subject"])[0][0].decode(),
        }
        info['letter_body'] = await self.subject(num)
        return info
