from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectDetailView

from . import views

urlpatterns = [
    path("list/", views.project_list, name="project_list"),
    path("list/short", views.project_list, {"is_short": True}, name="project_list_short"),
    path("detail/<int:pk>", ProjectDetailView.as_view(), name="project_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)