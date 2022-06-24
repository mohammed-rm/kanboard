from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from . import views

app_name = 'plugin'

urlpatterns = [
    path('', views.login_form, name='login'),
    path('accueil', views.accueil, name='accueil'),
    path('ajout-tache', views.TacheAjout.as_view(), name='ajout-tache'),
    path('selection-taches', views.TacheListe.as_view(), name='selection-taches'),
    path('cra', views.cra, name='cra'),
    path('pdf', views.GenererPDF.as_view(), name='pdf'),

]

urlpatterns += staticfiles_urlpatterns()
