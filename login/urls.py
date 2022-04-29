from django.urls import path
from .views import createUserPage, loginPage, logoutPage

urlpatterns = [

    path('login/', loginPage, name='login'),
    path('cadastro-user/', createUserPage, name='cadastro-user'),
    path('logout/', logoutPage, name='logout')
    
]