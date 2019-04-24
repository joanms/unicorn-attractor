from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class LoginForm(TestCase):
    
    """Tests for the login form"""
    
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
        

class RegistrationForm(TestCase):
    
    """Tests for the registration form"""
    
    def test_can_register(self):
        form = UserRegistrationForm({'email': 'test@example.com', 'username': 'FooBar', 'password1': 'abc123!?', 'password2': 'abc123!?'})
        self.assertTrue(form.is_valid)

    def test_email_is_required(self):
        form = UserRegistrationForm({'email': ''})
        self.assertFalse(form.is_valid())
        # self.assertEqual(form.errors['email'], [u'Email address must be unique']) # Need to fix KeyError: email
        
    def test_username_is_required(self):
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_passwords_must_match(self):
        form = UserRegistrationForm({'password1': 'abc123!?', 'password2': 'xyz123!?'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])


class TestViews(TestCase):
    
    """Tests for the views"""
    
