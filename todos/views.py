from datetime import date
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from .models import Todo

# Create your views here.

# Versao Manual de Listagem exemplo 01
""" def home(request):
    # return HttpResponse("Olá Mundo!!!")
    return render(request, "todos/home.html") """


# VIEW BASEADA EM FUNÇÃO EXEMPLO 01 FUNCIONAL
""" def todo_list(request):
    Passando parametro direto
    nome = "Emerson"
    alunos = ["Elton Fonseca", "Ariel Sardinha", "Anna Beatriz"]

    todos = Todo.objects.all  # consegue manipular o banco trazendo tudo com o ALL
    return render(request, "todos/todo_list.html", {"todos": todos}) """


# VIEW BASEADA EM CLASSE EXEMPLO 02 FUNCIONAL
class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    # Campos que permitimos preencher
    fields = ["title","deadline"]
    # Definindo a URL
    success_url = reverse_lazy("todo_list")
    
class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")
    
class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

""" classe funcional com a regra para verificar 
se a tarefa foi concluida. """
# class TodoCompleteView(View):
#    def get(self, request, pk):
#        todo = get_object_or_404(Todo, pk=pk)
#        todo.finished_at = date.today()
#        todo.save()
#        return redirect("todo_list")

class TodoCompleteView(View):
   def get(self, request, pk):
       todo = get_object_or_404(Todo, pk=pk)
       todo.mark_has_complete()
       return redirect("todo_list")