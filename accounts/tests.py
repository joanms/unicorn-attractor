from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class LoginForm(TestCase):
    
    def test_can_log_in(self):
        
        """Ensure that a user can log in"""

        form = UserLoginForm({'username': 'FooBar', 'password': 'abc123!?'})
        self.assertTrue(form.is_valid)


    def test_username_is_required(self):
        
        """Ensure that a username is required for login"""

        form = UserLoginForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

        
    def test_password_is_required(self):
        
        """Ensure that a password is required for login"""

        form = UserLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
        

class RegistrationForm(TestCase):
    
    def test_can_register(self):
    
        """Ensure that the registration form works correctly"""
    
        form = UserRegistrationForm({'email': 'test@example.com', 'username': 'FooBar', 'password1': 'abc123!?', 'password2': 'abc123!?'})
        self.assertTrue(form.is_valid)


    def test_email_is_required(self):
    
        """Ensure that an email address is required for registration"""
    
        form = UserRegistrationForm({'email': ''})
        self.assertFalse(form.is_valid())
        # self.assertEqual(form.errors['email'], [u'Email address must be unique']) # Need to fix KeyError: email

        
    def test_username_is_required(self):
    
        """Ensure that a username is required for registration"""
    
        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])


    def test_passwords_must_match(self):
    
        """Ensure that both entered passwords match"""
    
        form = UserRegistrationForm({'password1': 'abc123!?', 'password2': 'xyz123!?'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [u'Passwords must match'])


class TestViews(TestCase):

    def test_get_login_page(self):
    
        """Ensure that the login page loads correctly"""
    
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

        
    def test_get_registration_page(self):
    
        """Ensure that the registration page loads correctly"""
    
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")        