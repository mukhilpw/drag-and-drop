"""
URL configuration for datasave project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# urls.py
from django.urls import path
from .views import save_card,card_manager,get_cards,card_history,delete_card

urlpatterns = [
    path('get-cards/', get_cards, name='get_cards'),
    path('save-card/', save_card, name='save_card'),
    path('card-manager/', card_manager, name='card_manager'),
    path('card-history/', card_history, name='card_history'),
    path('delete-card/<int:card_id>/', delete_card, name='delete_card'),
    # Other paths...
]




