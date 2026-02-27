"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from rest_framework import routers
from . import views
import os
from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'users', views.UserProfileViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

def custom_api_root(request, format=None):
    CODESPACE_NAME = os.environ.get('CODESPACE_NAME')
    base_url = request.build_absolute_uri('/')
    if CODESPACE_NAME:
        base_url = f'https://{CODESPACE_NAME}-8000.app.github.dev/'
    return views.api_root(request._request, format=format)._replace(headers={'Location': base_url})

from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/api/', permanent=False)),
    re_path(r'^api/$', views.api_root, name='api-root'),
    path('api/', include(router.urls)),
]
