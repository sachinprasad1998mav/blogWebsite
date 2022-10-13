from unicodedata import category
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import home, category, post, about


urlpatterns = [
    path('', home),
    path('about/',about),
    path('blog/<slug:url>',post),
    path('category/<slug:url>',category),
    path("accounts/", include("django.contrib.auth.urls")),
] 