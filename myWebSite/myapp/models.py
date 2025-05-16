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
    project_short_text = models.TextField(default="")
    project_text = models.TextField(default="")
    project_link = models.TextField(default="")
    project_client = models.TextField(default="")
    project_github_link = models.TextField(default="")
    project_image = models.ImageField(upload_to = "projects")
    project_type = models.CharField(choices =TYPE_OF_PROJECT_CHOICES, default= PERSONAL, max_length=100)
    project_date = models.DateField("date published")
    
    def __str__ (self):
        return self.project_title
# Create your models here.
class Stack(models.Model):
    stack_name = models.CharField(max_length=30)

    def __str__(self):
        return self.stack_name


class Profile(models.Model):
    profile_name = models.CharField(max_length=100)
    profile_description = models.TextField(default="")
    profile_image = models.ImageField(upload_to="profile")
    profile_stack = models.ManyToManyField(Stack,blank=False)
    
    def __str__(self):
        return self.profile_name

class Experiences(models.Model):
    xp_enterprise = models.CharField(max_length=100)
    xp_start_date = models.DateField()
    xp_end_date = models.DateField(blank=True, null=True)
    xp_description = models.TextField()
    xp_stack = models.ManyToManyField(Stack)

    def __str__(self):
        return self.xp_enterprise


