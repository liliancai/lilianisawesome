from accounts.models import Token
import sys
from accounts.models import User


class PasswordlessAuthenticationBackend(object):
	
	def authenticate(self,uid):
		#if not token.filter.exist() return None
		#token=get(uid)
		#try user=get(email)
		#except DoesNotExst,create
		if not Token.objects.filter(uid=uid).exists():
			print('Token doesnt exist',file=sys.stderr)
			return None
		token=Token.objects.get(uid=uid)
		print('got token',file=sys.stderr)
		try:
			user=User.objects.get(email=token.email)
			print('got user')
			return user
		except User.DoesNotExist:
			print('new user')
			return User.objects.create(email=token.email)


	def get_user(self,email):
		try:
			return User.objects.get(email=email)
		except User.DoesNotExist:
			return None
