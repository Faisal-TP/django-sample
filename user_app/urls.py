from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('login',LoginView.as_view(),name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('create', views.createFn,name='create'),
    path('createaccount', views.createaccount,name='createaccount'),
]
