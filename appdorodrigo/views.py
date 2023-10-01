from django.shortcuts import render, redirect
from .models import Paisagens, Curiosidades

def home(request):
  paisagem = Paisagens.objects.all()
  curiosidades = Curiosidades.objects.all()
  print(paisagem)
  print(curiosidades)
  
  return render(request,"home.html",context={"paisagens":paisagem,"curiosidades":curiosidades})

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

def delete_paisagem(request,id):
  paisagem = Paisagens.objects.get(id = id)
  if request.method == "POST":    
    if request.POST['confirm']:
      paisagem.delete()
    
    return redirect("home")
  return render(request,'are_you_sure.html',context={"paisagem":paisagem})

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

def delete_curiosidade(request,id):
  curiosidade = Curiosidades.objects.get(id=id)
  if request.method == "POST":   
    if request.POST['confirm']:
      curiosidade.delete()
  
    return redirect("home")
  return render(request,'are_you_sure2.html',context={"curiosidade":curiosidade})