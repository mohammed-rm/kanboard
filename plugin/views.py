from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic import View

from .models import Utilisateur
from .logic.services import *
from .pdf import generer_en_pdf

taches_globale = Tache()
dure_globale = dict[str, int]


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
    template_name = 'plugin/ajout_tache.html'
    success_url = reverse_lazy('plugin:taches-liste')


class TacheListe(ListView):
    model = Tache
    template_name = 'plugin/selection_taches.html'


def cra(request):
    date = request.POST.get('start')

    annee = conversion_annee(date)
    mois = conversion_mois(date)

    taches = get_par_date(annee, mois)
    duree = total_mensuel_formatter(annee, mois)

    global taches_globale
    taches_globale = taches

    global dure_globale
    dure_globale = duree

    context = ({
        "TACHES": taches,
        "DUREE": duree,
    })

    return render(request, 'plugin/cra.html', {'CONTEXT': context})


class GenererPDF(View):
    @staticmethod
    def get(*args, **kwargs):
        pdf = generer_en_pdf('plugin/pdf.html', {"TACHES": taches_globale, "DUREE": dure_globale})
        return HttpResponse(pdf, content_type='application/pdf')
