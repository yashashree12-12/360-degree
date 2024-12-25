from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dash'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('fitness/', views.fitness, name='fitness'),
    path('logout/', views.logout_view, name='logout'),
]
