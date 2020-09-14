from django.urls import path
from django.views.generic.base import RedirectView

from . import views

app_name = 'orderly'


urlpatterns = [

    path('', RedirectView.as_view(url='engineer/list', permanent=False), name='index'),

    path('engineer/list', views.EngineerList.as_view(), name='engineer_list'),
    path('engineer/create', views.EngineerCreate.as_view(), name='engineer_create'),

]
