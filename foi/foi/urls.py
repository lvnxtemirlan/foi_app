from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f"foi/admin/", admin.site.urls),
    path(f"foi/", include("signin.urls")),
]
