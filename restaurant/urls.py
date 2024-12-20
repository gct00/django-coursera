from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name="home"),  # Página inicial será o menu
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),  # Adicionando a URL para o menu
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
]
