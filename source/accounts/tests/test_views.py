#test after sending email if the webpage redirect to homepage
from unittest.mock import patch
from django.test import TestCase
from unittest import skip
import accounts.views
from accounts.models import Token
Testemail="liliancai404@gmail.com"

class SendLoginEmailViewTest(TestCase):
	#@skip
	def test_redirects_to_home_page(self):
		response=self.client.post('/accounts/login?token=abcd123')
		self.assertRedirects(response, '/')


	def test_creates_token_associated_with_email(self):
		self.client.post('/accounts/send_login_email',data={
			'email':Testemail
		})
		token=Token.objects.first()

		self.assertEqual(token.email,Testemail)
	
	@patch('accounts.views.send_mail')
	def test_sends_link_to_login_using_token_uid(self,mock_send_mail):
		self.client.post('/accounts/send_login_email',data={
			'email':Testemail
		})
		token=Token.objects.first()
		expected_url=f'http://testserver/accounts/login?token={token.uid}'
		(subject,body,from_email,to_email),kwargs=mock_send_mail.call_args
		self.assertIn(expected_url,body)




	def test_adds_success_message(self):
		
		response=self.client.post('/accounts/send_login_email',data={
			'email':'test@mockto.com'
		},follow=True)

		message=list(response.context['messages'])[0]
		self.assertEqual(
			message.message,
			"Check your email, we've sent you a link you can use to log in."
		)
		self.assertEqual(message.tags,"success")

	@patch('accounts.views.auth')
	def test_calls_authenticate_with_uid_from_get_request(self,mock_view_auth):
	#mock authenticate() cus login used  auth.authenticate()
	#better don't over test authenticate to much
	#so mock views.au here,just check if the call_args equal to call(uid)
	#see if the token=abc123 in url arrive authenticate() or not
	#just test the api here and leave the detail in authenticate's own ut
		self.client.get('/accounts/login?token=abc123')
		self.assertEqual(mock_view_auth.authenticate.call_args,call(uid='abc123'))'

		
