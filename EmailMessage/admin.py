from django.contrib import admin
from .models import EmailAccount


@admin.register(EmailAccount)
class EmailAccountAdmin(admin.ModelAdmin):
    class Meta:
        model = EmailAccount
        fields = '__all__'


