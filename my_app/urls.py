from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('home', views.myhome,name='my home'),
    path('add', views.add,name='add'),
    path('add2', views.add2,name='add2'),
    path('addnos', views.addnos,name='addnos'),
    path('addnos2', views.addnos2,name='addnos2'),

    # path('admin',views.admin)
]
