#test after sending email if the webpage redirect to homepage
from unittest.mock import patch
from django.test import TestCase
from unittest import skip
import accounts.views

class SendLoginEmailViewTest(TestCase):
	#@skip
	def test_redirects_to_home_page(self):
		response=self.client.post('/accounts/login?token=abcd123')
		self.assertRedirects(response, '/')


	@patch('accounts.views.send_mail')	
	def test_sends_mail_address_from_post(self,mock_send_mail):

		'''
		def fake_send_mail(subject,body,from_email,to_list):
			self.send_mail_called=True
			self.subject=subject
			self.body=body
			self.from_email=from_email
			#I wanna chang this to_list to to_email!
			self.to_list=to_list
		'''

		self.client.post('/accounts/send_login_email',data={
			'email':'test@mockto.com'
		})
		#then check the email content is what supposed to or not
		self.assertTrue(mock_send_mail.send_mail_called)
		(subject,body,from_email,to_email),kwargs=mock_send_mail.call_args
		self.assertEqual(subject,'Your log in link from todolist')
		self.assertEqual(from_email,'test@mockfrom.com')
		self.assertEqual(to_email,['test@mockto.com'])


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
