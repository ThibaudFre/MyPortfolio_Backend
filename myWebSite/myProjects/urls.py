from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.project_list, name="project_list"),
    path("detail/", views.detail, name="project_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)