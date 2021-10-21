from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('add', views.add),
    path('display', views.loadfun),
    path('displaydata', views.displaydata),
    path('deletedata', views.deletedata,name='deletedata'),
    path('viewsingle', views.fnviewsingle,name='viewsingle'),
    path('fileupload', views.fnfileupload,name='fileupload'),
]

