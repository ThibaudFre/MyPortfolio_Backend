from django.db import models

class Project(models.Model):
    PERSONAL = "PERS"
    PROFESSIONAL = "PRO"
    FORMATION = "FORM"
    
    TYPE_OF_PROJECT_CHOICES = {
        "PERSONAL": "Personel",
        "PROFESSIONAL": "Professionel",
        "FORMATION": "Formation",
    }
    
    
    project_title = models.CharField(max_length=100)
    project_text = models.TextField()
    project_link = models.TextField(default="")
    project_image = models.ImageField(upload_to = "projects")
    project_type = models.CharField(choices =TYPE_OF_PROJECT_CHOICES, default= PERSONAL, max_length=100)
    project_date = models.DateTimeField("date published")
    
    def __str__ (self):
        return self.project_title
# Create your models here.
