from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name="login"),
    path('sign_up/', views.userSignUp, name='sign_up'),
    path('logout/', views.userLogout, name='logout')
]