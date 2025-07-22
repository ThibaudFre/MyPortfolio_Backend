from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectDetailView, ProfilDetailView, StackListView

from . import views

urlpatterns = [
    path("profile/<int:pk>", ProfilDetailView.as_view(), name="profile"),
    path("projectlist/", views.project_list, name="project_list"),
    path("projectlist/short", views.project_list, {"is_short": True}, name="project_list_short"),
    path("detail/<int:pk>", ProjectDetailView.as_view(), name="project_detail"),
    path("stacklist/", StackListView.as_view(), name="stack_list")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)