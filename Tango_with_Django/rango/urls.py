from django.urls import path
from . import views
# to setup media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("category/<str:category_name_url>", views.show_category, name="show_category"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)