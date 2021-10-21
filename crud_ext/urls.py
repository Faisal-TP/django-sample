from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('register', views.register,name='register'),
    path('viewrecords', views.viewrecords,name='viewrecords'),
    path('delete/<int:id>', views.delete,name='delete'),
    path('viewsingle/<int:id>', views.viewsingle,name='viewsingle'),
    path('update/<int:id>', views.update,name='update'),
    path('login', views.login,name='login'),
    path('home', views.home,name='home'),
    path('profile', views.profile,name='profile'),
    # path('addnos2', views.addnos2,name='addnos2')
    path('test3', views.FnBase,name='test3'),
    path('index',views.index,name='index')
]
