from django.urls import path, include
from django.contrib import admin
from accounts import views as acc_views

urlpatterns = [
    path('dashboard/', acc_views.dashboard, name='dashboard'), 
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('admin/', admin.site.urls),
]
