"""django_example URL Configuration

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
from django.urls import path,include

#upload image display
from django.conf.urls.static import static
from django.conf import settings
#close upload image display

#api
# from .router import router
#api

urlpatterns = [
    #path('',include('my_app.urls')),
    path('crud/',include('crud_ext.urls')),
    path('Ajax_crud/',include('Ajax_crud.urls')),
    path('django_api/',include('django_api.urls')),
    path('django_user/',include('user_app.urls')),
    # path('api/',include('router.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
#for image display
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)