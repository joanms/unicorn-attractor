from django.test import TestCase
from .forms import BugReportForm, CommentForm


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

        
    def test_get_bug_report_page(self):
    
        """Ensure that the bug report form page loads correctly"""
    
        page = self.client.get("/bugs/report_bug/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "report_bug.html")                
