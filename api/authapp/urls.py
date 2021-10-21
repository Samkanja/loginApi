from django.urls import include, path
from authapp import views

urlpatterns = [
    path('',include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]