"""introduce_jinyoung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import myapp.views
import portfolio.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #myapp앱에 해당되는 urls
    path('', myapp.views.main, name="main"),
    path('profile/', myapp.views.profile, name="profile"),
   
    #portfolio앱에 해당되는 url
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)