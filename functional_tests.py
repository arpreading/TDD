from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        #check homepage of new online to-do app
        self.browser.get('http://localhost:8000')


        #Noticing the page title and header mentions to-do lists
        self.assertIn ('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn ('To-Do', header_text)

        #Invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
            )

        #Types in "finish learning javascript"(To add to fullstack cv)"
        inputbox.send_keys('Finish learning Javascript')

        #When hitting enter page updates and now the page lists:
        #"1, Finish learning Javascript" as an item on the to-do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Finish learning Javascript' for row in rows),
            "New to-do item did not appear in table"
            )

        #There is still a text box inviting the user to enter another item
        #enters "use code to make a dynamic website"
        self.fail('Finish the test!')

        #The page updates again and shows both items on the list

        #User wonders whether the site will remember the list.
        #A unique URL has been generated -- there is some explanatory text
        #to that effect.

        #Visiting the URL the user can see that the to-do list is still there

if __name__=='__main__':
    unittest.main(warnings='ignore')


