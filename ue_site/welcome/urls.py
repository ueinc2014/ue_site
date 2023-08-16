from django.urls import path

from welcome.views import index

app_name = "welcome"

urlpatterns = [
    path('', index),
]