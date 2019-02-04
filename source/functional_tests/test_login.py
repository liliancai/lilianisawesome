from django.core import mail
from selenium.webdriver.common.keys import Keys 
import re
from .base import FunctionalTest
import time

TEST_EMAIL = 'liliancai@404@gmail.com'
SUBJECT="Your log in link from todolist"

class LoginTest(FunctionalTest):

	def test_can_get_email_link_to_log_in(self):
		#send email
		self.browser.get(self.live_server_url)
		#time.sleep(30)
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
		print('url is \n',url)
		#act as click in
		self.browser.get(url)

		
		#okay not logged in
		self.wait_for(
			lambda:self.browser.find_element_by_link_text('Log out')
		)

		navbar=self.browser.find_element_by_css_selector('.navbar')
		self.assertIn(TEST_EMAIL,navbar.text)
		
		#test log out works by click()
		self.browser.find_element_by_link_text('Log out').click()	
		#test if 'enter enamil to login' show up again by find 'email'
		#and also make sure the test_email address didn't show up on homeapge
		self.wait_for(
			lambda:self.browser.find_element_by_name('email')
		)

		navbar=self.browser.find_element_by_css_selector('.navbar')
		self.assertNotIn(TEST_EMAIL,navbar.text)
		
