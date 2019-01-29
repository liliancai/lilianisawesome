#test after sending email if the webpage redirect to homepage
from django.test import TestCase
from unittest import skip
import accounts.views

class SendLoginEmailViewTest(TestCase):
	#AssertionError: 301 != 302 : Response didn't redirect as expected: Response code was 301 (expected 302)
	#page 324, test later
	#I know what's wrong, is url again!!!!!!!!!!!
	#okay, in the urls.py I written the url(r'^send_login_email/$')
	#after remove the '/' this test passed and as fake_send_mail got called, 
	#okay, always double check syntax error, and triple check url!
	#peace out~
	#@skip
	def test_redirects_to_home_page(self):
		response=self.client.post('/accounts/send_login_email',data={
			'email':'test@test.com'
			})
		self.assertRedirects(response, '/')

	def test_sends_mail_address_from_post(self):
		#you wouldn't wanna use the real email-send function
		#so we need write a mock email-send function same with the one in view
		#to test without mess the real email address

		self.send_mail_called=False

		#like a reciever recieing all the attributes from send_email()
		#then use assertEqual to check if the send_email() pass all the right content
		#okay, but what's the point?????
		#cus if use email.to, have to accually use emailbox as reciever
		#which will produce tons of junk email
		#so fake send mail function accually send those mail content to testcase itself instead of calling send_email to send real mail box
		#mocking here is acctually replace the email send api~
		def fake_send_mail(subject,body,from_email,to_list):
			self.send_mail_called=True
			self.subject=subject
			self.body=body
			self.from_email=from_email
			#I wanna chang this to_list to to_email!
			self.to_list=to_list


		accounts.views.send_mail=fake_send_mail

		#then call the link!
		#but one question here,how can send_login_email call views.send_email,urls???
		#okay,I get now, cus of 'import accounts.views!', so the namespacing contains accounts.views.send_email
		self.client.post('/accounts/send_login_email',data={
			'email':'test@mockto.com'
		})
		#then check the email content is what supposed to or not

		self.assertTrue(self.send_mail_called)
		self.subject='Your login link from todolist'
		#self.body=
		self.from_email='test@mockfrom.com'
		self.to_list='test@mockto.com'
