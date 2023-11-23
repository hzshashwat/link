from django.urls import path
from .views import update_links

urlpatterns = [
    path('', update_links, name='update_links')
]