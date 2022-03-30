"""cloud_note URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # user--匹配到user/之后，交友user下面的应用去处理
    path('user/', include('user.urls')),
    path('index/', include('index.urls')),
    path('note/', include('note.urls')),
    path('test_cache', views.test_cache),
    path('test_mw', views.test_mw),
    path('test_csrf', views.test_csrf),
    path('test_page', views.test_page),
    path('test_csv', views.test_csv),
    path('make_page_csv', views.make_page_csv)
]
