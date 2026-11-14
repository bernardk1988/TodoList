
from django.urls import path
from . import views
from .api_views import TodoAPI,TodoDetailAPI


urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('edit/<int:id>/',views.edit_todo, name='edit_todo'),
    path('delete/<int:id>/',views.delete_todo,name='delete_todo'),
    path('api/todos/', TodoAPI.as_view(), name='todo_api'),
    path('api/todos/<int:id>/',TodoDetailAPI.as_view(),name='todo_detail_api'),
]
