from django.urls import path

from .views import homePgeView

urlpatterns = [
    path('', homePgeView, name='home')
]