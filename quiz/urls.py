
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls'), name="main"),
    path('game-admin/', admin.site.urls),
]
