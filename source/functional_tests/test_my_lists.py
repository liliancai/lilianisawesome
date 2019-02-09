#a new FT for test my lists
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY,SESSION_KEY,get_user_model
from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest
User=get_user_model()
TEST_EMAIL = 'liliancai@404@gmail.com'

class MyListTest(FunctionalTest):
	
	def create_pre_authenticated_session(self,email):
		#use email to create session, and use add_session to add user,session,path
		#bond session with user,create a user,create a user,sessionkey=pk,backendsessionkey=authenticationbackends
		user=User.objects.create(email=email)
		session=SessionStore()
		session[SESSION_KEY]=user.pk
		session[BACKEND_SESSION_KEY]=settings.AUTHENTICATION_BACKENDS[0]
		session.save()

		#add_session to browser
		#get url by 404 cus it's the fastest,add_cookie
		self.browser.get(self.live_server_url+"/404_no_such_url/")
		self.browser.add_cookie(dict(
			name=settings.SESSION_COOKIE_NAME,
			value=session.session_key,
			path='/',
		))


	'''	
	#get url,log out, call create,go back,wait_to_be_logged_in
	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		self.browser.get(self.live_server_url)
		self.wait_to_be_logged_out(TEST_EMAIL)

		self.create_pre_authenticated_session(email=TEST_EMAIL)
		self.browser.get(self.live_server_url)
		self.wait_to_be_logged_in(email=TEST_EMAIL)
	'''
	#create session tested
	def test_logged_in_users_lists_are_saved_as_my_lists(self):
		self.create_pre_authenticated_session(TEST_EMAIL)

		self.browser.get(self.live_server_url)
		self.add_list_item('dumplings')
		self.add_list_item('flour')
		#self.add_list_item('flour')

		first_list_url=self.browser.current_url

		self.browser.find_element_by_link_text('My Lists').click()

		self.wait_for(
			lambda:self.browser.find_element_by_link_text('dumplings')
		)

		self.browser.find_element_by_link_text('dumplings').click()

		self.wait_for(
			lambda:self.assertEqual(self.browser.current_url,first_list_url)
		)

		#second list and check again, then log out
		self.browser.get(self.live_server_url)
		self.add_list_item('Buns')
		second_list_url=self.browser.current_url

		self.browser.find_element_by_link_text('My Lists').click()

		self.wait_for(
			lambda:self.browser.find_element_by_link_text('Buns')
		)

		self.browser.find_element_by_link_text('Buns').click()

		self.wait_for(
			lambda:self.assertEqual(self.browser.current_url,second_list_url)
		)

		self.browser.find_element_by_link_text('Log out').click()

		'''
		self.wait_for(
			lambda:self.assertEqual(
				self.browser.find_element_by_link_text('My Lists'),
				[]
		))
		'''


