from django.http import HttpResponse, JsonResponse
from django.views.generic.detail import DetailView
from myapp.models import Project


#def index(request):
#    return HttpResponse("Hello, world. You're at my Projects page.")
# Create your views here.

class ProjectDetailView (DetailView):
    model = Project;

    def render_to_response(self, context, **response_kwargs):
        project = self.get_object()
        data = {
            "id": project.id,
            "title": project.project_title,
            "text": project.project_text,
            "link": project.project_link,
            "githubLink": project.project_github_link,
            "client": project.project_client,
            "date": project.project_date 
        }
        return JsonResponse(data, **response_kwargs)


def index(request):
    return HttpResponse("Hello, world. You're at my index's page.")

def detail(request, project_id):
    project = Project.objects.filter(id = project_id)
    return JsonResponse(project)



def project_list(request, is_short=False):
    if is_short:
        project = Project.objects.values("project_title", "project_image", "project_type")
        return JsonResponse(list(project), safe=False)
    project = Project.objects.values("project_title", "project_image","project_short_text", "project_type")
    return JsonResponse(list(project), safe=False)


