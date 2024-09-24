from django.db import models


class EmailAccount(models.Model):
    # модель для данных почты
    PROVIDER_CHOICES = [
        ('yandex.ru', 'yandex.ru'),
        ('gmail.com', 'gmail.com'),
        ('mail.ru', 'mail.ru'),
    ]
    email = models.EmailField(unique=True, verbose_name='email')
    password = models.CharField(max_length=255, verbose_name='password')
    provider = models.CharField(max_length=50, choices=PROVIDER_CHOICES, verbose_name='provider')

    class Meta:
        verbose_name = "Email account"
        verbose_name_plural = "Email accounts"

    def __str__(self):
        return self.email

class EmailMessage(models.Model):
    # модель для данных письма
    email_account = models.ForeignKey(EmailAccount, on_delete=models.CASCADE, verbose_name='email name')
    subject = models.TextField(null=True, blank=True, verbose_name='subject')
    send_date = models.DateTimeField()
    receive_date = models.DateTimeField(auto_now_add=True, verbose_name='receive date')
    message_body = models.TextField(null=True, blank=True, verbose_name='body')
    attachments = models.JSONField(null=True, blank=True, verbose_name='attachments')

    class Meta:
        verbose_name = "Email message"
        verbose_name_plural = "Email messages"

    def __str__(self):
        return self.subject or 'No Subject'
