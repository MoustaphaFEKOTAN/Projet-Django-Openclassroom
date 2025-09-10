"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from listings import views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),  # <-- toutes les routes allauth
    path('admin/', admin.site.urls),
    path('', views.band_list, name='band-list'),
    path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('listing/band/<int:band_id>/', views.band_listing, name='band-listing'),
    path('band/<int:band_id>/update', views.band_update, name='band-update'),
    path('band/<int:band_id>/delete', views.band_delete, name='band-delete'),
    path('contact-us/', views.contact, name='contact'),
    path('listing/', views.articles),
    path('about-us/', views.about),
]
