from rest_framework import authentication
from rest_framework.serializers import Serializer
from fs.decorators import unauthenticated_user
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib.auth.models import User



from . models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect, resolve_url


import random
from django.db.models import Q, F


@login_required(login_url='connexion')
def Dashboard(request):
    
    if request.user.is_staff:

        
        client = Client.objects.filter(agent__user__is_superuser = 0).all().count()
          
        agent = Agent.objects.filter(user__is_superuser = 0).all().count()
    

    else:

        client = Client.objects.filter(Q(agent=request.user.agent)).all().count()
        
        
    
    return render(request, 'default/dashboard.html', locals())




#--------------------------AGENT----------------------------#
@login_required(login_url='connexion')
def ajouter_employe(request):
    
    #Invoquer les 2 formulaires, et les afficher comme un seul formulaire sur la page html
    form_user = FormeUser(data=request.POST)
    form_employe = AgentForm(data=request.POST)

    if request.method == 'POST':
        #Verifier la concordance des deux mots de passe
        password1 = request.POST.get('password')
        password2 = request.POST.get('passwordCheck')
        
        contact = request.POST.get('contact')
        if password1 != password2:
            passwordDontMatch = True
            return render(request, 'default/ajouter_agent.html', 
            {'Les deux mot de passe ne sont pas identiques':passwordDontMatch})

        #Verifier la validité des 2 formulaire
        if form_user.is_valid() and form_employe.is_valid():
            prenoms = form_employe.cleaned_data['prenom']
            nom = form_employe.cleaned_data['nom']
            
            #Verifier que le contact est unique
            if Agent.objects.filter(contact=contact):
                ContactExist = True
                return render(request, 'default/ajouter_agent.html', 
            {'Le contact existe':ContactExist})

            username = nom + str(random.randint(0,100))
            while User.objects.filter(username=username):
                username = nom + str(random.randint(0,100))
        
            #Ajouter un employé et enregistrer
            user = User.objects.create_user(username=username, first_name=prenoms, last_name=nom, password=password1)
            group = Group.objects.get(name='agent')
            user.groups.add(group)
            user.save() 

            
            employe = form_employe.save(commit=False)

            #Set One to One relationship between FormeUser and FormeEmploye
            employe.user = user

            #Maintenant enregistrons le model
            employe.save()

            #Ajout réussi
            return HttpResponseRedirect(reverse('liste_agent'))

    context = {'form':form_employe, 'form2':form_user}      
    #Si ca n'a pas été un post Http, on va alors afficher une page blanche
    return render(request,'default/ajouter_agent.html', context)


#Voir les détails sur un employe
@login_required(login_url='connexion')
def detail_employe(request, pk, opt=None):
    
    employe = Agent.objects.get(id=pk)
    option = request.POST.get('option')
    if opt == 'delete':
        employe.delete()
        return redirect('liste_agent')
    return render(request, 'marine/detail_agent.html', locals())


#Mettre a jour le profil d'un employé
@login_required(login_url='connexion')
def maj_profil_employe(request, pk):
    employe = get_object_or_404(Agent, id=pk)
    if request.method == 'POST':
        user_form = FormeUser(request.POST, instance=employe.user)
        employe_form = AgentForm(
            request.POST, instance=employe)
        if user_form.is_valid() and employe_form.is_valid():
            user = user_form.save()
            user.set_password(request.POST.get('password'))
            user.save()
            employe_form.save()
            #Rediriger vers la liste des employés
            return redirect('liste_employe')
    else:
        user_form = FormeUser(instance=request.user)
        employe_form = AgentForm(instance=request.user.utilisateur)

    context = {
        'user_form': user_form,
        'employe_form': employe_form,
    }
    return render(request, 'default/edite_agent.html', locals())


#@login_required(login_url='connexion')
def ListeAgent(request):
   
    #Ce tag affiche la liste de tous les employés
    liste_employe = Agent.objects.filter(Q(user__is_superuser = 0)).all()
    
    return render(request, 'default/liste_agent.html', locals())



#@login_required(login_url='connexion')
def ProfilAgent(request, pkey):
    
    profile = Agent.objects.get(id=pkey)

    client = profile.client_set.all()

    context = {'profil':profile,'client':client,}

    
    return render(request, 'default/profil_agent.html', context)


#La vue pour se connecter
@unauthenticated_user
def connexion(request):
    login_form = AuthenticationFormWithContact(request.POST or None)
    redirect_to = request.GET.get('next', '')
    if request.method == 'POST' and login_form.is_valid():
        login(request,request, login_form.get_user)
        # Send the user back to some page.
        return HttpResponseRedirect(redirect_to)
    return render(request, 'default/auth-signin.html')

#La vue pour se deconnecter
@login_required(login_url='connexion')
def deconnexion(request):

    logout(request)
    return HttpResponseRedirect(reverse(connexion))


#--------------------------CLIENT----------------------------#

@login_required(login_url='connexion')
def AjouterClient(request):

    form = ClientForm()
    
    if request.method == 'POST':
        form = ClientForm(request.POST,)
        nom = request.POST.get('nom_client')
        prenom =request.POST.get('Prénoms_client')
        zone = request.POST.get('zone')
        agent = request.user.agent

        if form.is_valid():

            obj = Client.objects.create(
                nom_client = nom , Prénoms_client = prenom, zone = zone,
                agent = agent,
            )
            obj.save()

        return redirect('liste_client')

    context = {'form':form}
    return render(request, 'default/ajouter_client.html', context) 



#@login_required(login_url='connexion')
def ModifierClient(request, pkey):
   
    client  = Client.objects.get(id=pkey)
    form = ClientForm(instance=client)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
        return redirect('profil_client', client.id)
            
    context = {'form':form}
    return render(request, 'default/ajouter_client.html', context)        


#@login_required(login_url='connexion')
def SupprimerClient(request, pkey):

    client = Client.objects.get(id=pkey)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_client')

    context = {'client':client}
    return render(request, 'default/supprimerClient.html', context) 


#@login_required(login_url='connexion')
def ProfilClient(request, pkey):
    profile = Client.objects.get(id=pkey)

    context = {'profil':profile}
    return render(request, 'default/profil_client.html', context)



#@login_required(login_url='connexion')
def ListeClient(request):
    profile = request.user.agent

    if request.user.is_staff:
        client = Client.objects.all().order_by('agent')
        myfilter = ClientFilter(request.GET, queryset=client)
        client = myfilter.qs
    else:
        client = Client.objects.filter(agent=profile).order_by('-nom_client')
        myfilter = ClientFilter2(request.GET, queryset=client)
        client = myfilter.qs
    

    context =  {'client':client, 'myfilter':myfilter}
    return render(request, 'default/liste_client.html', context)



@login_required(login_url='connexion')
def ClientResidence(request, pkey):
   
    client  = Client.objects.get(id=pkey)
    form = ResidenceForm(instance=client)
    if request.method == 'POST':
        form = ResidenceForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            print("yes")
        return redirect('profil_client', client.id)
            
    context = {'form':form}
    return render(request, 'default/client_residence.html', context)


def ImageResidence(request, pkey):
   
    client  = Client.objects.get(id=pkey)
    form = ImageResidenceForm(instance=client)
    if request.method == 'POST':
        form = ImageResidenceForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            print("yes")
        return redirect('profil_client', client.id)
            
    context = {'form':form}
    return render(request, 'default/image_residence.html', context)



#@login_required(login_url='connexion')
def ImprimerClient(request, pkey):
   
    client  = Client.objects.get(id=pkey)
    
    context = {'form':client}
    return render(request, 'default/imprimer_client.html', context)
 

