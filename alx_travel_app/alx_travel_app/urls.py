from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to ALX Travel App!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # This replaces the Django welcome page
]
