from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from oc_lettings_site import settings
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("sentry_debug/",views.sentry_debug, name="debug")
]
