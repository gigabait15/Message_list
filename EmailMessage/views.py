from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from EmailMessage.forms import EmailAccountForm
from EmailMessage.models import EmailMessage, EmailAccount
from EmailMessage.serializers import EmailMessageSerializer


# ViewSet объектов класса EmailMessage
class EmailMessageViewSet(viewsets.ModelViewSet):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer


# Genegic для отображения списка объектов EmailAccount
class EmailAccountListView(generic.ListView):
    model = EmailAccount
    template_name = 'EmailMessage/email_account_list.html'
    context_object_name = 'email_accounts'

# Genegic для создания объектов EmailAccount
class EmailAccountCreateView(generic.CreateView):
    model = EmailAccount
    template_name = 'EmailMessage/email_account_create.html'
    fields = ['email', 'password', 'provider']
    success_url = reverse_lazy('email_account_list')

# Genegic для удаления объектов EmailAccount
class EmailAccountDeleteView(generic.DeleteView):
    model = EmailAccount
    template_name = 'EmailMessage/email_account_confirm_delete.html'
    success_url = reverse_lazy('email_account_list')

def email_select_view(request):
    email_accounts = EmailAccount.objects.all()
    return render(request, 'EmailMessage/email_select.html', {'email_accounts': email_accounts})

def base(request):
    return render(request, 'EmailMessage/base.html')



