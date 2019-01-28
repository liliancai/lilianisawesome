from django.core import mail
from selenium.webdriver.common.keys import Keys 
import re

from .base import FunctionalTest

TEST_EMAIL = 'liliancai@404@gmail.com'
SUBJECT="Your login link for todolist"

class LoginTest(FunctionalTest):

	def test_can_get_email_link_to_log_in(self):
		#send email
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_name('email').send_keys(TEST_EMAIL)
		self.browser.find_element_by_name('email').send_keys(Keys.ENTER)

		#check if the email sent or not by 'Check your email'
		self.wait_for(lambda:self.assertIn(
			'Check your email',
			self.browser.find_element_by_tag_name('body').text
		))

		#get the mailbox and check it's email 
		email=mail.outbox[0]
		self.assertIn(TEST_EMAIL,email.to)
		self.assertEqual(email.subject,SUBJECT)

		#check the url sent or not
		self.assertIn('Use this link to log in',email.body)
		url_search=re.search(r'http://.+/.+$',email.body)

		if not url_search:
			self.fail(f'Could not find url in email body:\n{email.body}')
		url=url_search.group(0)
		self.assertIn(self.live_server_url,url)

		#act as click in
		self.browser.get(url)

		
		#okay not logged in
		self.wait_for(
			lambda:self.browser.find_element_by_link_text('Log out')
		)

		navbar=self.browser.find_element_by_css_selector('.navbar')
		self.assertIn(TEST_EMAIL,navbar.text)
		