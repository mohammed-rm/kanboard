from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Utilisateur, Tache


def login_form(request):
    return render(request, 'plugin/login.html')


def accueil(request):
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    mot_de_passe = request.POST.get('password')

    utilisateur = Utilisateur(nom=nom, prenom=prenom, mot_de_passe=mot_de_passe)

    return render(request, 'plugin/accueil.html', {'UTILISATEUR': utilisateur})


class TacheAjout(CreateView):
    model = Tache
    fields = '__all__'
    template_name = 'plugin/ajout-tache.html'
    success_url = reverse_lazy('plugin:taches-liste')


class TacheListe(ListView):
    model = Tache
    template_name = 'plugin/taches_liste.html'
