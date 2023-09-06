from django.urls import path
from jinja2_app import views

urlpatterns = [
    path('',views.base, name='base'),
    path('child_temp/',views.child, name='base'),
    path('home_temp/',views.home, name='home'),
    path('home_tabl/',views.table_home, name='tbl'),
    path('home_text/',views.text_home, name='txt'),
    path('about/',views.about, name='abt'),
    path('contact/',views.contact, name='cont'),
    path('index/',views.index, name='in'),
]
