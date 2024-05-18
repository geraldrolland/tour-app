from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutUs, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('explore/', views.explore, name='explore'),
    path('book/', views.book, name='book'),
    path('experience', views.experience, name='experience'),
    path('help/', views.help, name='help'),
    path('paypal/pay/<pk>/', views.pay, name="pay"),
    path('paypal/create/<id>/', views.create, name="paypal-create"),
    path('paypal/<order_id>/capture/<id>/', views.capture, name="paypal-capture"), #changed #
    path('paypal/client-id/', views.getClientId , name="client-id"),
    path('upload/', views.upload_image, name='upload')
]
