from django.urls import path
from todolist.views import show_todolist, task_toggle, task_delete, login_user, register, create_task, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('toggle-task/<int:id>', task_toggle, name='toggle_task'),
    path('delete-task/<int:id>', task_delete, name='delete_task'),
]

