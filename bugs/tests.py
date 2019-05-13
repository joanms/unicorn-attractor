from django.test import TestCase
from .forms import BugReportForm, CommentForm
from django.contrib.auth.models import User


class TestForms(TestCase):

    def test_can_report_bug(self):
        
        """Ensure that a user can report a bug"""

        form = BugReportForm({'title': 'Unicorns', 'description': 'Too many unicorns.'})
        self.assertTrue(form.is_valid)

    def test_can_comment_on_a_bug(self):
        
        """Ensure that a user can report a bug"""

        form = CommentForm({'text': 'I like the unicorns.'})
        self.assertTrue(form.is_valid)
        
        
class TestViews(TestCase):
    
    def test_get_bug_list_page(self):
    
        """Ensure that the bug list page loads correctly"""
    
        page = self.client.get("/bugs/view_bugs/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "view_bugs.html")

        
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