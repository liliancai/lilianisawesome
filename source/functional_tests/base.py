from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import time
MAX_WAIT = 10	

class FunctionalTest(StaticLiveServerTestCase): 
	def setUp(self): 
		self.browser = webdriver.Firefox() 
		self.browser.implicitly_wait(30)
	def tearDown(self): 
	    self.browser.quit()

	#a decorator as wait
	def wait(fn):
		def modified_fn(*args,**kwargs):
			start_time=time.time()
			while True:
					try:
						return fn(*args,**kwargs)
					except (AssertionError,WebDriverException) as e:
						if  time.time()-start_time>MAX_WAIT:
								raise e
						time.sleep(0.5)
		return modified_fn

	@wait
	def wait_for_row_in_list_table(self,row_text):
		table=self.browser.find_element_by_id('id_list_table')
		rows=table.find_elements_by_tag_name('tr')
		self.assertIn(row_text,[row.text for row in rows])

	@wait
	def wait_for(self,fn):
		return fn()

	def get_item_input_box(self):
		return self.browser.find_element_by_id('id_text')

	#write wait_for as decorator
	#add 2 FTs as check if logged in and out, and use the 2 new FTs in test_my_list, and use then in test_login 

	@wait
	def wait_to_be_logged_in(self,email):
		self.browser.find_element_by_link_text('Log out')
		navbar=self.browser.find_element_by_css_selector('.navbar')
		self.assertIn(email,navbar.text)

	@wait
	def wait_to_be_logged_out(self,email):
		self.browser.find_element_by_name('email')
		navbar=self.browser.find_element_by_css_selector('.navbar')
		self.assertNotIn(email,navbar.text)
