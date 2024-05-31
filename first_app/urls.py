from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.form,name = 'form'),
    path('signup/',views.employ_form,name = 'model_form')
]