from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.
