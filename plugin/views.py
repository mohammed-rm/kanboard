from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic import View

from .models import Utilisateur, Tache
from .pdf import generer_en_pdf


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
    annee_str, mois_str, mois_final_str = "", "", ""

    for nombre in range(4):
        annee_str += date[nombre]
    for nombre in range(5, 7):
        mois_str += date[nombre]

    if mois_str[0] == '0':
        mois_final_str = mois_str[1]
    else:
        mois_final_str = mois_str

    annee = int(annee_str)
    mois = int(mois_final_str)

    taches = Tache.get_par_date(annee, mois)
    duree = Tache.total_mensuel_formatter(annee, mois)
    pdf = generer_en_pdf('plugin/pdf.html')
    context = ({
        "LISTE": taches,
        "DURATION": duree,
        "PDF": pdf
    })

    return render(request, 'plugin/cra.html', {'CONTEXT': context})


class GeneratePdf(View):
    @staticmethod
    def get(*args, **kwargs):
        pdf = generer_en_pdf('plugin/pdf.html')
        return HttpResponse(pdf, content_type='application/pdf')

