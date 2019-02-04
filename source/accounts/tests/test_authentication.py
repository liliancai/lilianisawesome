from unittest import TestCase
from accounts.models import Token
from django.contrib.auth import get_user_model
from accounts.authentication import PasswordlessAuthenticationBackend
User=get_user_model()
#check if uid exist
#check if user exist
#if uid exist but not user,create one



class AuthenticateTest(TestCase):

	def test_returns_None_if_no_such_token(self):
		result=PasswordlessAuthenticationBackend().authenticate('No such token')
		self.assertIsNone(result)

	def test_returns_new_user_with_correct_email_if_token_exists(self):
		#create a token,input email,get the new user,check return_value equal to the new user or not and email
		email='anewguy@accounts.ut'
		token=Token.objects.create(email=email)
		user=PasswordlessAuthenticationBackend().authenticate(token.uid)
		new_user=User.objects.get(email=email)
		self.assertEqual(user,new_user)
		#self.assertEqual(newuser.email,email)

	def test_returns_existing_user_with_correct_email_if_token_exists(self):
		email='anoldpal@accounts.ut'
		existing_user=User.objects.create(email=email)
		token=Token.objects.create(email=email)
		user=PasswordlessAuthenticationBackend().authenticate(token.uid)
		self.assertEqual(user,existing_user)


class GetUserTest(TestCase):
	#but why a new get_user function, better explicit than implicit???
	
	def test_gets_user_by_email(self):
	#create a user named desired_user, and call get_user to get a found_user
	#desired_user is supposed to equal to found_user

			email='testgetuserbyemail@accounts.ut'
			desired_user=User.objects.create(email=email)
			found_user=PasswordlessAuthenticationBackend().get_user(email)
			self.assertEqual(desired_user,found_user)

	def test_returns_None_if_no_user_with_that_email(self):
	#get_user without create one before, assertEqual()
			email='doesnotexist@accounts.ut'
			self.assertIsNone(PasswordlessAuthenticationBackend().get_user(email=email))
			

