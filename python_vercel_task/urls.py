from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return HttpResponse("<h1>¡Bienvenido a Django en Vercel!</h1>")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
