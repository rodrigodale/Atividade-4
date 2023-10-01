from django.shortcuts import render, redirect
from .models import Paisagens, Curiosidades
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
  paisagem = Paisagens.objects.all()
  curiosidades = Curiosidades.objects.all()
  print(paisagem)
  print(curiosidades)
  
  return render(request,"home.html",context={"paisagens":paisagem,"curiosidades":curiosidades})

@login_required
def create_paisagem(request):
  if request.method == "POST":
    Paisagens.objects.create(
      nome_da_paisagem = request.POST["paisagem"],
      localizacao = request.POST["localizacao"],
    clima = request.POST["clima"],
    altitude = request.POST["altitude"]
    )

    return redirect("home")
  return render(request,'forms.html',context={"action":"Adicionar"})

@login_required
def update_paisagem(request,id):
  paisagem = Paisagens.objects.get(id = id)
  if request.method == "POST":
    paisagem.nome_da_paisagem = request.POST["nome_da_paisagem"]
    paisagem.localizacao = request.POST["localizacao"]
    paisagem.clima = request.POST["clima"]
    paisagem.altitude = request.POST["altitude"]
    paisagem.save()
      
    return redirect("home")
  return render(request,'forms.html',context={"paisagem":paisagem,"action":"Atualizar"})

@login_required
def delete_paisagem(request,id):
  paisagem = Paisagens.objects.get(id = id)
  if request.method == "POST":    
    if request.POST['confirm']:
      paisagem.delete()
    
    return redirect("home")
  return render(request,'are_you_sure.html',context={"paisagem":paisagem})

@login_required
def create_curiosidade(request):
  if request.method == "POST":
    Curiosidades.objects.create(
      nome_da_paisagem = request.POST["nome_da_paisagem"],
      frequencia = request.POST["frequencia"],
    prioridade_de_visita = request.POST["prioridade_de_visita"],
    categoria = request.POST["categoria"]
    )

    return redirect("home")
  return render(request,'forms2.html',context={"action":"Adicionar"})

@login_required
def update_curiosidade(request,id):
  curiosidade = Curiosidades.objects.get(id=id)
  if request.method == "POST":
    curiosidade.nome_da_paisagem = request.POST["nome_da_paisagem"]
    curiosidade.frequencia = request.POST["frequencia"]
    curiosidade.prioridade_de_visita = request.POST["prioridade_de_visita"]
    curiosidade.categoria = request.POST["categoria"]
    curiosidade.save()
  
    return redirect("home")
  return render(request,'forms2.html',context={"curiosidade":curiosidade,"action":"Atualizar"})

@login_required
def delete_curiosidade(request,id):
  curiosidade = Curiosidades.objects.get(id=id)
  if request.method == "POST":   
    if request.POST['confirm']:
      curiosidade.delete()
  
    return redirect("home")
  return render(request,'are_you_sure2.html',context={"curiosidade":curiosidade})


def create_user(request):
  if request.method == "POST":
    user = User.objects.create_user(
      request.POST["username"],
      request.POST["email"], 
      request.POST["password"]
    )
    user.save()
    return redirect("home")
  return render(request, "register.html", context={"action": "Adicionar"})


def login_user(request):
  if request.method == "POST":
    user = authenticate(
      username = request.POST["username"],
      password = request.POST["password"]
    )

    if user != None:
      login(request, user)
    else:
      return render(request, "login.html", context={"error_msg": "Usuário não existe"})
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
      return redirect("home")
    return render(request, "login.html", context={"error_msg": "Usuário não pode ser autenticado"})
  return render(request, "login.html")

def logout_user(request):
  logout(request)
  return redirect("login")