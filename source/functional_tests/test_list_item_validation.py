from selenium.webdriver.common.keys import Keys
from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):
	def test_cannot_add_empty_list_items(self):
		#try end a empty item to start a new list
		self.browser.get(self.live_server_url)
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

		#it supposed to have error message
		
		self.wait_for(lambda:self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You can't enter an empty list item"
		))

		#try end a empty item at a exsited list

		# She tries again with some text for the item, which now works    
		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		# Perversely, she now decides to submit a second blank list item
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		# She receives a similar warning on the list page
		self.wait_for(lambda: self.assertEqual(
			self.browser.find_element_by_css_selector('.has-error').text,
			"You can't have an empty list item"
		))
		# And she can correct it by filling some text in
		self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
		self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)
		self.wait_for_row_in_list_table('1: Buy milk')
		self.wait_for_row_in_list_table('2: Make tea')
		


