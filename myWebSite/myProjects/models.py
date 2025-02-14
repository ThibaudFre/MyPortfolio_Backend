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
    project_image = models.ImageField(upload_to = "projects")
    project_type = models.Charfield(choices =TYPE_OF_PROJECT_CHOICES, default= PERSONAL)
    project_date = models.DateTimeField("date published")
# Create your models here.
