from django.urls import path
from . import views
from .views import scatter_view



urlpatterns = [
path('', views.home, name='home'),
path('scatter/', scatter_view, name='scatter'),
]