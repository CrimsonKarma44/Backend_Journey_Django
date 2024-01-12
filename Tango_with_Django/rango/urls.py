from django.urls import path
from . import views
# to setup media
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("category/<str:category_name_url>", views.show_category, name="show_category"),
    path("add_category/", views.add_category, name="add_category"),
    path("<str:category_name_slug>/add_page", views.add_page, name="add_page"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)