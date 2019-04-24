from django.test import TestCase
from .forms import UserLoginForm

# Create your tests here.
class LoginForm(TestCase):
    
    def test_can_log_in(self):
        form = UserLoginForm({'username': 'FooBar', 'password': 'abc123!?'})
        self.assertTrue(form.is_valid)
        
    def test_username_is_required(self):
        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])
        
    def test_password_is_required(self):
        form = UserLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])        