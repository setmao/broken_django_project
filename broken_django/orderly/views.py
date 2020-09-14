from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .models import Engineer


# Create your views here.
class EngineerList(ListView):
    model = Engineer


class EngineerCreate(CreateView):
    model = Engineer
    fields = ['name', 'nickname']
    success_url = reverse_lazy('orderly:engineer_list')
