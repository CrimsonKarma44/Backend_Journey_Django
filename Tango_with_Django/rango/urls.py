from django.urls import path
from . import views
# to setup media
from django.conf import settings
from django.conf.urls.static import static

# app_name = 'rango'
# if you add the app_name then add the value of the app_name to every url you make in the html like {% url 'app_name:...' %}
# usuall the best practice when working with multiple apps

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("category/<str:category_name_url>", views.show_category, name="show_category"),
    path("add_category/", views.add_category, name="add_category"),
    path("<str:category_name_slug>/add_page", views.add_page, name="add_page"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)