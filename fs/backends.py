from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

from .models import Agent

class MyBackend(BaseBackend):

    def authenticate(self, request, **kwargs):
        contact = kwargs['contact']
        password = kwargs['password']
        try:
            user = Agent.objects.get(contact=contact).user
            if user.check_password(password) is True:
                return user
            
            return None
        except Agent.DoesNotExist:
            return None

    def get_user(self, contact):
        try:
            return Agent.objects.get(pk=contact).user
        except User.DoesNotExist:
            return None


