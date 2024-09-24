from django.urls import path
from .apps import EmailmessageConfig
from .views import (
    base,
    email_select_view,
    EmailAccountCreateView,
    EmailAccountDeleteView,
    EmailAccountListView)

app_name = EmailmessageConfig.name


urlpatterns = [
    path('', base, name='start_link'),
    path('select-email/', email_select_view, name='email_select'),
    path('email_account_list/', EmailAccountListView.as_view(), name='email_account'),
    path('create/', EmailAccountCreateView.as_view(), name='email_account_create'),
    path('delete/<int:pk>/', EmailAccountDeleteView.as_view(), name='email_account_delete'),
]
