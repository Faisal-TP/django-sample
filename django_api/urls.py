from django.urls import path
from . import views
# from django.viewsets import RegisterViewSet
urlpatterns = [
    path('', views.index,name='index'),
    path('getdata', views.getdata,name='getdata'),
    # path('viewrecords', views.viewrecords,name='viewrecords'),
    path('deldata', views.deldata,name='deldata'),
    # path('viewsingle/<int:id>', views.viewsingle,name='viewsingle'),
    # path('update/<int:id>', views.update,name='update'),
    # path('login', views.login,name='login'),
    # path('home', views.home,name='home'),
    # path('profile', views.profile,name='profile'),
    # path('addnos2', views.addnos2,name='addnos2')
]
