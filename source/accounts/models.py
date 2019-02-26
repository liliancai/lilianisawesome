from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.contrib import auth
auth.signals.user_logged_in.disconnect(auth.models.update_last_login)	
# Create your models here.

'''
class User(models.Model):
	email=models.EmailField(primary_key=True)
	REQUIRED_FIELDS=[]
	USERNAME_FIELD='email'
	is_anonymous=False
	is_authenticated=True
'''

	# For createsuper or djangoadmin
	# It's better extend auth.model User

class User(AbstractUser):
	# default password as pass
	email=models.EmailField(primary_key=True)
	REQUIRED_FIELDS=[]
	USERNAME_FIELD='username'
	
	REQUIRED_FIELDS = ['email']

	is_anonymous=False
	is_authenticated=True


class Token(models.Model):
	email=models.EmailField()
	uid=models.CharField(default=uuid.uuid4,max_length=40)
