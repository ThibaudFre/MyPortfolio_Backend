from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at my index's page.")

def detail(request):
    return HttpResponse("Hello, world. You're at my detail's project page.")

def project_list(request, isShort=None):
    if(isShort == "short"):
        return HttpResponse("Short data's project has been requested");
    return HttpResponse("Full data's project has been requested");