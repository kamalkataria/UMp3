
from django.urls import path
from .views import index,process

app_name = "youtubetomp3"

urlpatterns = [
    path("", index, name="index"),
    path('youtubetomp3/process',process,name='process'),
]