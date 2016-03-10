from django.conf.urls import url
from mails import views

urlpatterns = [
    url(r'^message$', views.message, name='message'),
]
