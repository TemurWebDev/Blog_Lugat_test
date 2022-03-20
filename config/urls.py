"""config URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from translate.views import translate_view
from blog.views import home_blog_view,complete_blog_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('translate/',translate_view,name='translate-url'),

    # path('',home_blog_view,name='home-url'),
    # path('r/<int:pk>',complete_blog_view,name='complate-url'),
    # path('r/<int:pk>/delete/',PostDeleteview.as_view(),name='delete-url'),
]
