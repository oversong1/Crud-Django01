from django.contrib import admin
from django.urls import path

# VIEW BASEADA EM FUNÇÃO EXEMPLO 01 FUNCIONAL
# from todos.views import todo_list

# VIEW BASEADA EM CLASSE EXEMPLO 02 FUNCIONAL
from todos.views import (
    TodoListView, 
    TodoCreateView, 
    TodoUpdateView, 
    TodoDeleteView,
    TodoCompleteView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", todo_list),
    # path('create', TodoCreateView.as_view()),
    path("", TodoListView.as_view(), name='todo_list'),
    path('create', TodoCreateView.as_view(), name='todo_create'),
    path("update/<int:pk>", TodoUpdateView.as_view(), name='todo_update'),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name='todo_delete'),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name='todo_complete'),
]
