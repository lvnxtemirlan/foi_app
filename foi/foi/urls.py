from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path(f"admin/", admin.site.urls),
    path(f"", include("signin.urls")),
]
