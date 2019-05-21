from django.test import TestCase, Client
from .forms import FeatureReportForm, FeatureCommentForm
from django.contrib.auth.models import User
from .models import Feature


class TestForms(TestCase):

    def test_can_report_feature(self):
        
        """Ensure that a user can report a feature"""

        form = FeatureReportForm({'title': 'Unicorns', 'description': 'Too many unicorns.'})
        self.assertTrue(form.is_valid)


    def test_can_comment_on_a_feature(self):
        
        """Ensure that a user can comment on a feature"""

        form = FeatureCommentForm({'text': 'I like the unicorns.'})
        self.assertTrue(form.is_valid)


    def test_title_is_required(self):

        """Ensure that the feature report form requires a title"""

        form = FeatureReportForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], [u'This field is required.'])

        
    def test_description_is_required(self):
        
        """Ensure that the bug report form requires a description"""

        form = FeatureReportForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['description'], [u'This field is required.'])
        
        
class TestViews(TestCase):
    
    def setUp(self):
        
        """
        Set up temporary users and a feature for testing purposes. Code by Marcin Mrugacz: 
        https://github.com/Migacz85/django_app/blob/master/features/tests.py
        """
        
        self.user = User.objects.create(
            username='admin',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password("asdfg")
        self.user.save()

        self.user = User.objects.create(
            username='John',
            password='asdfg',
            is_active=True,
            is_staff=True,
            is_superuser=False
        )
        self.user.set_password("asdfg")
        self.user.save()
        
        self.client = Client()
        self.feature = Feature.objects.create(
            title='test',
            description='this is a test',
            submitter=self.user
        )
        self.feature.save()


    def test_get_feature_list_page(self):
    
        """Ensure that the feature list page loads correctly"""
    
        page = self.client.get("/features/list_features/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "list_features.html")

    def test_get_feature_detail_page(self):
    
        """Ensure that the feature detail page loads correctly"""
    
        page = self.client.get("/features/{}/".format(self.feature.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "feature_details.html")

        
    def test_feature_report_requires_login(self):
    
        """Ensure that the feature report form is only accessible to logged in users"""
    
        response = self.client.get("/features/request_feature/")
        self.assertRedirects(response, '/accounts/login/?next=/features/request_feature/')

        
    def test_commenting_requires_login(self):
    
        """Ensure that commenting is only accessible to logged in users"""
    
        response = self.client.get("/features/comment/1/")
        self.assertRedirects(response, '/accounts/login/?next=/features/comment/1/')                

        
    def test_feature_report_form_loads_correctly(self):
    
        """Ensure that the feature report form loads correctly when a user is logged in"""
    
        self.client.login(username='John', password='asdfg')
        response = self.client.get("/features/request_feature/")
        self.assertEqual(response.status_code, 200)

        
    def test_commenting_form_loads_correctly(self):
    
        """Ensure that the commenting form loads when a user is logged in"""
    
        self.client.login(username='John', password='asdfg')
        response = self.client.get("/features/comment/{}/".format(self.feature.id))
        self.assertEqual(response.status_code, 200)