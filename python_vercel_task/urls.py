from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse



def home(request):
    return HttpResponse("¡Bienv¿")


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
