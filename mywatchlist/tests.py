from django.test import TestCase, Client

# Create your tests here.
class UnitTestURL(TestCase):

    def test_html_valid(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200, 'HTTP 200 OK')

    def test_xml_valid(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200, 'HTTP 200 OK')
    
    def test_json_valid(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200, 'HTTP 200 OK')
    
    def test_app_uses_template(self):
        response = Client().get('/mywatchlist/')
        self.assertTemplateUsed(response, 'mywatchlist.html')
