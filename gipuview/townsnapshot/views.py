from django.shortcuts import render
from townsnapshot.models import Municipio,Tipo,Stats
# Create your views here.
from django.views.generic.detail import DetailView


class MunicipioDetailView(DetailView):

    model = Municipio

    def get_context_data(self, **kwargs):
        context = super(MunicipioDetailView, self).get_context_data(**kwargs)
	municipio = context['object']
	city_stats = Stats.objects.filter(municipio=municipio.id)
        stats = {}
	for tipo in Tipo.objects.all():
	    stats[tipo.name] = city_stats.get(tipo=tipo.id).metros
	context["stats"] = stats
        print context
        return context
