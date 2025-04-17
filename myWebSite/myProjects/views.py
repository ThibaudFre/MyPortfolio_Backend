from django.http import HttpResponse
from myprojects.models import Project


#def index(request):
#    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at my index's page.")

def detail(request):
    return HttpResponse("Hello, world. You're at my detail's project page.")

def project_list(request, isShort=None):
    if(isShort == "short"):
        project = Project.objects.values("project_title", "project_image")
        return project;
    project = Project.objects.values("project_title", "project_image",)
    return project;