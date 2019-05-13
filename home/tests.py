from django.test import TestCase

class TestViews(TestCase):
    
    def test_get_index_page(self):
    
        """Ensure that the index page loads correctly"""
    
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
