from django.shortcuts import render
from townsnapshot.models import Municipio
# Create your views here.
from django.views.generic.detail import DetailView


class MunicipioDetailView(DetailView):

    model = Municipio

    def get_context_data(self, **kwargs):
        context = super(MunicipioDetailView, self).get_context_data(**kwargs)
        return context
