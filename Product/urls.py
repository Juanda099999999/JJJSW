from unicodedata import name
from django.urls import path
from JJSW2 import views

urlpatterns = [
    path('<slug:slug>',views.ProductDetailView.as_view(),name='product'),
    
    
]