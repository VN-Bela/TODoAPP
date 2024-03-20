from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path("",views.home,name="home"),
   path("login/",views.login,name="login"),
   path("signup/",views.signup,name="signup"),
   path("todo_add/",views.todo_add,name="todo_add"),
   path("logout/",views.signout,name="logout"),
   path("delete_todo/<int:id>",views.delete_todo,name="delete_todo"),
   path("todo_done/<int:id>/<str:status>",views.todo_done,name="todo_done"),
]






