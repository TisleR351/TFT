"""
URL configuration for apitft project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from tisfittracker.views import MachineExerciseViewSet

router = DefaultRouter()

api_urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-token-auth/", views.obtain_auth_token),
    path("accounts/", include("rest_registration.api.urls")),
    path(
        "machine_exercise/",
        MachineExerciseViewSet.as_view({"get": "list", "post": "create"}),
        name="machine-exercise-list",
    ),
    path(
        "machine_exercise/<int:pk>/",
        MachineExerciseViewSet.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
        name="machine-exercise-detail",
    ),
]

urlpatterns = [
    path("api/v1/", include(api_urlpatterns)),
]
