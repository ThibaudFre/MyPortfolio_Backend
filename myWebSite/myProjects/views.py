from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.

def detail(request):
    return HttpResponse("Hello, world. You're at my detail's project page.")

def project_list(request):
    return HttpResponse("Hello, world. You're at my projects List page.")