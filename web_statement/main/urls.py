from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_bids, name='home'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('create_jango/', views.create_jango, name='create_jango'),
    path('create_html/', views.create_html, name='create_html'),
    path('<int:pk>', views.Bid_edit.as_view(), name='bid_edit'),
]
