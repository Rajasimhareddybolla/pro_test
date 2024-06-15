from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name=""),
    path('greet', views.greet, name='home'),
    # add more paths here
]