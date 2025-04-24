from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProjectDetailView

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/<str:isShort>", views.project_list, name="project_list_short"),
    path("list/", views.project_list, name="project_list"),
    path("<int:pk>/detail/", ProjectDetailView.as_view(), name="project_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)