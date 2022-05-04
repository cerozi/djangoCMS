from django.urls import path
from .views import homeView, productsList, userHomeView, productCreate

urlpatterns = [ 
    path('', homeView, name='home'),
    path('user/', userHomeView, name='user'),

    path('produtos/', productsList.as_view(), name='products'),
    path('produtos/criar/', productCreate.as_view(), name='criar-produto'),
]