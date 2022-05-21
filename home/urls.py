from django.urls import path
from .views import homeView, userHomeView

urlpatterns = [ 
    # ADMIN home;
    path('', homeView, name='home'),
    # CUSTOMER home;
    path('user/', userHomeView, name='user'),
]
