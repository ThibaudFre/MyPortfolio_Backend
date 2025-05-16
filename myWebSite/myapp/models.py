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
    
    
    title = models.CharField(max_length=100)
    short_text = models.TextField(default="")
    text = models.TextField(default="")
    link = models.TextField(default="")
    client = models.TextField(default="")
    github_link = models.TextField(default="")
    image = models.ImageField(upload_to = "projects")
    type = models.CharField(choices =TYPE_OF_PROJECT_CHOICES, default= PERSONAL, max_length=100)
    date = models.DateField("date published")
    
    def __str__ (self):
        return self.project_title
# Create your models here.
class Stack(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.stack_name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="profile")
    stack = models.ManyToManyField(Stack,blank=False)

    
    def __str__(self):
        return self.profile_name

class Experiences(models.Model):
    enterprise = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    stack = models.ManyToManyField(Stack)

    def __str__(self):
        return self.xp_enterprise


