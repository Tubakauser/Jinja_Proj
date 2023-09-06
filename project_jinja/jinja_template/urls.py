from django.urls import path
from jinja_template import views

urlpatterns = [
    path('forloop/',views.for_loop, name='for'),
    path('forcounter0/',views.for_counter0, name='counter0'),
    path('forfirst/', views.for_first, name='first'),
    path('forlast/', views.for_last, name='last'),
    path('forparent/', views.for_parent, name='parent'),
]