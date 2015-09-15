from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import TestCase, Client
from account import views
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from account.hash import UserHasher


class IndexViewTest(StaticLiveServerTestCase):
    fixtures = ['users.json']

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_reach_index_page_and_log_in(self):
        self.browser.get(self.live_server_url)

        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango', body.text)

        # testing username and password
        username_field = self.browser.find_element_by_name('username')
        username_field.send_keys('lade')

        password_field = self.browser.find_element_by_name('password')
        password_field.send_keys('password')
        password_field.send_keys(Keys.RETURN)

        # username and password accepted
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Codango Home', body.text)


class PasswordResetTestCase(TestCase):
    
    def setUp(self):
        # create a test client:
        self.client = Client()
        # register a sample user:
        self.user_account = User.objects.create_user('inioluwafageyinbo', 'inioluwafageyinbo@gmail.com', 'codango')
        self.user_account.first_name = 'Inioluwa'
        self.user_account.last_name = 'Fageyinbo'
        self.user_account.save()

    def test_get_returns_200(self):
        response = self.client.get('/recovery/')
        self.assertEquals(response.status_code, 200)

    def test_post_returns_200(self):
        response = self.client.get('/recovery/')
        self.assertEquals(response.status_code, 200)

    def test_recovery_email_sent_for_registered_user(self):
        response = self.client.post('/recovery/', {"email": self.user_account.email})
        self.assertIn("email_status", response.context)

    def test_recovery_email_not_sent_for_unregistered_user(self):
        response = self.client.post('/recovery/', {"email":"fagemaki.iniruto@gmail.com" })
        self.assertNotIn('email_status', response.context)