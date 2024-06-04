from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from tickets.models import Organisation


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            organisation = Organisation.objects.create(name=user.username)

            user.organisation = organisation
            user.save()

            return redirect('login')

    form = UserForm()
    context = {"form": form}
    return render(request, 'account/register.html', context)


def connect(request):
    #     if request.method=='POST':
    #         username = request.POST.get("username")
    #         password = request.POST.get("password")
    #
    #         user = authenticate(request , username=username , password=password)
    #         if user is not None:
    #             login(request , user )
    #             organisation_name = user.username
    #             return redirect(f'/{organisation_name}/')
    #         else:
    #             messages.info(request , "votre nom d'utilisateur ou votre mot de passe est incorrect")
    #
    #         print(username)
    #         print(password)
    #     return render(request , "account/login.html")
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                # Redirigez l'utilisateur vers une page après la connexion
                return redirect('organisation', username)  # Remplacez 'home' par l'URL de votre choix
    else:
        form = LoginForm()

        return render(request, 'account/login.html', {'form': form})

# Create your views here.
