from django.http import HttpResponse, JsonResponse
from django.views.generic.detail import DetailView
from myapp.models import Project,Profile


#def index(request):
#    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.

class ProjectDetailView (DetailView):
    model = Project;

    def render_to_response(self, context, **response_kwargs):
        project = self.get_object()
        data = {
            "id": project.id,
            "title": project.title,
            "text": project.text,
            "link": project.link,
            "image":project.image.url,
            "githubLink": project.github_link,
            "client": project.client,
            "date": project.date 
        }
        return JsonResponse(data, **response_kwargs)

class ProfileDetailView (DetailView):
    model = Profile

    def render_to_response(self, context, **response_kwargs):
        profile = self.get_object()
        stack_list = list(profile.stack.values_list('name', flat=True))
        data = {
            "name": profile.name,
            "description": profile.description,
            "image": profile.image.url,
            "stack": stack_list
        }
        return JsonResponse(data, **response_kwargs)


def project_list(request, is_short=False):
    if is_short:
        project = Project.objects.values("title", "image", "type")
        return JsonResponse(list(project), safe=False)
    project = Project.objects.values("title", "image","short_text", "type")
    return JsonResponse(list(project), safe=False)


