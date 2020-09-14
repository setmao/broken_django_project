from django.urls import path

from . import views

app_name = 'orderly'


urlpatterns = [

    path('engineer/list', views.EngineerList.as_view(), name='engineer_list'),
    path('engineer/create', views.EngineerCreate.as_view(), name='engineer_create'),

]
