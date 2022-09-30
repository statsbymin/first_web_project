"""mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf.urls.static import static  # add
from django.conf import settings            # add

from mini.views import HomeView  # add





urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.HomeView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('resume/', views.ResumeView.as_view(), name='resume'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio-details/', views.PortfoliodetailsView.as_view(), name='portfolio-details'),
    
    
    path('photo/', include('photo.urls')), # add
    

    # path('', views.AboutView.as_view(), name='about')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) # add





