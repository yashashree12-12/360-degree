from django.urls import path, include
from django.contrib import admin
from accounts import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
