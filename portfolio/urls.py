from portfolio import views
from django.urls import path
from .views import index

app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
]
