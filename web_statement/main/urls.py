from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('create_jango/', views.create_jango, name='create_jango'),
    path('create_html/', views.create_html, name='create_html'),
]



