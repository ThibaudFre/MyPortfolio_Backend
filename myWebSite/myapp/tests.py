from django.test import TestCase
from django.urls import reverse
from myapp.models import Project
from django.utils import timezone
from datetime import timezone as dt_timezone
import json





class ProjectTests(TestCase):
    def test_get_detail(self):
        project = Project.objects.create(
            project_title="Test Project",
            project_text="This is a test",
            project_link="https://example.com",
            project_github_link="https://github.com/example/project",
            project_client="Test Client",
            project_date= timezone.now()
        )

        url = reverse("project_detail", kwargs={"pk": project.id})
        response = self.client.get(url)

        expected_data = {
            "id": project.id,
            "title": project.project_title, 
            "text": project.project_text,
            "link": project.project_link,
            "githubLink": project.project_github_link,
            "client": project.project_client,
            "date": project.project_date.astimezone(dt_timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')
        }

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_short_data_project(self): 
        client = self.client;
        url = reverse("project_list_short");
        response = client.get(url);
        project = Project.objects.values("project_title", "project_image")
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))

    def test_get_full_data_project(self): 
        client = self.client;
        url = reverse("project_list");
        response = client.get(url);
        project = Project.objects.values("project_title", "project_image",)
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))
    
    

# Create your tests here.
