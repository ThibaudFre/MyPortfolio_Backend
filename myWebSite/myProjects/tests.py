from django.test import TestCase
from django.urls import reverse
from myprojects.models import Project
import json


class ProjectListRequestedTests(TestCase):
    def test_is_short_data_project_requested(self): 
        client = self.client;
        url = reverse("project_list_short", args=["short"]);
        response = client.get(url);
        project = Project.objects.values("project_title", "project_image")
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))

    def test_is_full_data_project_requested(self): 
        client = self.client;
        url = reverse("project_list");
        response = client.get(url);
        project = Project.objects.values("project_title", "project_image",)
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))
    
    

# Create your tests here.
