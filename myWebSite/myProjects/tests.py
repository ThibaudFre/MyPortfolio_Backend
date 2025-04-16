from django.test import TestCase
from news import views

class ProjectListRequestedTests(TestCase):
    def test_is_short_data_project_requested(self): 
        client = self.client;
        url = reverse("project_list_short", args=["short"]);
        response = client.get(url);
        self.assertEqual(response.content, "Short data's project has been requested")

    def test_is_full_data_project_requested(self): 
        client = self.client;
        url = reverse("project_list");
        response = client.get(url);
        self.assertEqual(response.content, "Full data's project has been requested")
        

# Create your tests here.
