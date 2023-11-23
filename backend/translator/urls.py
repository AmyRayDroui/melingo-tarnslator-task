from django.urls import path
from . import views 

urlpatterns = [
    path('translate/', views.get_word, name='translate'),
]