from django.test import TestCase, Client
from .forms import BugReportForm, BugCommentForm
from django.contrib.auth.models import User
from .models import Bug, BugUpvote


class TestForms(TestCase):

    def test_can_report_bug(self):
        
        """Ensure that a user can report a bug"""

        form = BugReportForm({'title': 'Unicorns', 'description': 'Too many unicorns.'})
        self.assertTrue(form.is_valid)

    def test_can_comment_on_a_bug(self):
        
        """Ensure that a user can comment on a bug"""

        form = BugCommentForm({'text': 'I like the unicorns.'})
        self.assertTrue(form.is_valid)
        
        
class TestViews(TestCase):
    
    def setUp(self):
        
        """
        Set up temporary users and a bug for testing purposes. 
        Code by Marcin Mrugacz: 
        https://github.com/Migacz85/django_app/blob/master/bugs/tests.py
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
        self.bug = Bug.objects.create(
            title='test',
            description='this is a test',
            submitter=self.user
        )
        self.bug.save()


    def test_get_bug_list_page(self):
    
        """Ensure that the bug list page loads correctly"""
    
        page = self.client.get("/bugs/list_bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "list_bugs.html")

    def test_get_bug_details_page(self):
    
        """Ensure that the bug detail page loads correctly"""
    
        page = self.client.get("/bugs/{}/".format(self.bug.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bug_details.html")

        
    def test_bug_report_requires_login(self):
    
        """Ensure that the bug report form is only accessible to logged in users"""
    
        response = self.client.get("/bugs/report_bug/")
        self.assertRedirects(response, '/accounts/login/?next=/bugs/report_bug/')

        
    def test_upvoting_requires_login(self):
    
        """Ensure that upvoting is only accessible to logged in users"""
    
        response = self.client.get("/bugs/upvote/1/")
        self.assertRedirects(response, '/accounts/login/?next=/bugs/upvote/1/')
        
        
    def test_commenting_requires_login(self):
    
        """Ensure that commenting is only accessible to logged in users"""
    
        response = self.client.get("/bugs/comment/1/")
        self.assertRedirects(response, '/accounts/login/?next=/bugs/comment/1/')                

        
    def test_bug_report_form_loads_correctly(self):
    
        """Ensure that the bug report form loads correctly when a user is logged in"""
    
        self.client.login(username='John', password='asdfg')
        response = self.client.get("/bugs/report_bug/")
        self.assertEqual(response.status_code, 200)

        
    def test_upvoting_works(self):
    
        """Ensure that upvoting works when a user is logged in"""
    
        self.client.login(username='John', password='asdfg')
        response = self.client.get("/bugs/upvote/{}/".format(self.bug.id))
        self.assertEqual(response.status_code, 200)
        
        
    def test_commenting_form_loads_correctly(self):
    
        """Ensure that the commenting form loads when a user is logged in"""
    
        self.client.login(username='John', password='asdfg')
        response = self.client.get("/bugs/comment/{}/".format(self.bug.id))
        self.assertEqual(response.status_code, 200)