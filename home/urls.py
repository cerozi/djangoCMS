from django.urls import path
from .views import homeView, userHomeView

urlpatterns = [ 
    path('', homeView, name='home'),
    path('user/', userHomeView, name='user'),
]