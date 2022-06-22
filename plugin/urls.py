from django.urls import path

from . import views

app_name = 'plugin'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('accueil', views.accueil, name='accueil'),
    path('ajout-tache', views.TacheAjout.as_view(), name='ajout-tache'),
    path('taches-liste', views.TacheListe.as_view(), name='taches-liste'),

]
