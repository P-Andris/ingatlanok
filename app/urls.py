from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('uj_ingatlan/', views.ujIngatlan, name = 'uj-ingatlan'),
    path('ingatlan_torlese/<int:id>', views.ingatlanTorlese, name = 'ingatlan-torlese')
]
