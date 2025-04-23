from django.http import HttpResponse, JsonResponse
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
    else:  
        project = Project.objects.values("project_title", "project_image","project_short_text")

    return JsonResponse(list(project), safe=False)
    

