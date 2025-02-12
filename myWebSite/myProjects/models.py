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
    project_type = models.Charfield(choices =TYPE_OF_PROJECT_CHOICES, default= PERSONAL)
    project_text = models.TextField()
# Create your models here.
