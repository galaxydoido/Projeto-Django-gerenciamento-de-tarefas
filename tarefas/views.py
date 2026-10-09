from django.shortcuts import render
from django.http import HttpResponse

def lista_tarefas(request):
   return render(request,'tarefas/lista_tarefas.html')

def form_tarefa(request):
   return render(request, 'tarefas/criar_tarefa.html')