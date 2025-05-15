# encurtador/urls.py

from django.contrib import admin
from django.urls import path
from urls.views import home, redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('<str:short_code>', redirect_view, name='redirect'),
]
