from django.test import TestCase
from django.urls import reverse
from myapp.models import Project, Stack
from django.utils import timezone
from datetime import timezone as dt_timezone, date
from django.core.files.uploadedfile import SimpleUploadedFile
import json





class ProjectTests(TestCase):
    def test_get_detail(self):
        project = Project.objects.create(
            title="Test Project",
            text="This is a test",
            link="https://example.com",
            github_link="https://github.com/example/project",
            image= SimpleUploadedFile(
                name="test_image.jpg",
                content=b'\x47\x49\x46\x38\x89\x61',
                content_type='image/jpeg'
            ),
            client="Test Client",
            date= date.today()
        )

        url = reverse("project_detail", kwargs={"pk": project.id})
        response = self.client.get(url)

        expected_data = {
            "id": project.id,
            "title": project.title, 
            "text": project.text,
            "link": project.link,
            "githubLink": project.github_link,
            "image": project.image.url,
            "client": project.client,
            "date":  project.date.isoformat()
        }

        print(response.json())

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    def test_get_short_data_project(self): 
        client = self.client;
        url = reverse("project_list_short");
        response = client.get(url);
        project = Project.objects.values("title", "image")
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))

    def test_get_full_data_project(self): 
        client = self.client;
        url = reverse("project_list");
        response = client.get(url);
        project = Project.objects.values("title", "image",)
        response_data = json.loads(response.content.decode())

        self.assertEqual(response_data, list(project))
    
    

class StackTests(TestCase):
    def test_get_stack(self):
        client = self.client;
        url = reverse("stack_list")
        response = client.get(url);
        stack = Stack.objects.all();
        response_data = json.loads(response.content.decode())
        self.assertEqual(response_data, list(stack))
    
class ProfilDetailTest(TestCase):
    def test_get_profile(self):
        client = self.client;
        url = reverse("my_profile", kwargs={"pk":1})
        response = client.get(url);
        profile = profile.objects.all();
        response_data = json.loads(response.content.decode())
        self.assertEqual(response_data, list(profile))
