from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from fs.forms import AuthenticationFormWithContact





urlpatterns = [

   path('tableau/', views.Dashboard, name="tableau"),

    #-----------------CONNEXION----------------#
   path('', auth_views.LoginView.as_view(template_name='default/auth-signin.html', authentication_form=AuthenticationFormWithContact), name='connexion'),
   path('accounts/logout/', auth_views. LogoutView.as_view(), name='deconnexion'),


   #-----------------AGENT----------------#
   path('profil_agent/<str:pkey>', views.ProfilAgent, name="profil_agent"),
   path('ajouter_agent/', views.ajouter_employe, name="ajouter_agent"),
   path('modifier_agent/<str:pkey>', views.maj_profil_employe, name="modifier_agent"),
   path('liste_agent/', views.ListeAgent, name="liste_agent"),
   #path('supprimer_agent/<str:pkey>', views.SupprimerAgent, name="supprimer_agent"),


   #---------------CLIENT-------------------#
   path('liste_client/', views.ListeClient, name="liste_client"),
   path('ajouter_client/', views.AjouterClient, name="ajouter_client"),
   path('modifier_client/<str:pkey>', views.ModifierClient, name="modifier_client"),
   path('supprimer_client/<str:pkey>', views.SupprimerClient, name="supprimer_client"),
   path('profil_client/<str:pkey>', views.ProfilClient, name="profil_client"),
   path('client_residence/<str:pkey>', views.ClientResidence, name="client_lieu_travail"),
   path('imprimer_client/<str:pkey>', views.ImprimerClient, name="imprimer_client"),
   path('image_residence/<str:pkey>', views.ImageResidence, name="image_residence"),





   
   
   

   
  

   

   
]
