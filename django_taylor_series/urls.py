"""
URL configuration for django_taylor_series project.

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

from django.urls import path, include
from main import views as main_views

urlpatterns = [
    path("", main_views.index_en),
    path("solve", main_views.solve_en),
    path("<str:lang>/", main_views.index),
    path("<str:lang>/solve/", main_views.solve),
]
