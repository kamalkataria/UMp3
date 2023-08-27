from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseNotFound
from django.http import HttpResponse
from .models import Filedownloaded
# Create your views here.
from pytube import YouTube
import os
from django.conf import settings

from django.templatetags.static import static
from pathlib import Path


def index(request):
    # print(request.GET['yturl'])
    return render(request=request, template_name="UMp3/index.html")


def process(request):
    yt = YouTube(request.GET.get('yturl'),use_oauth=False,allow_oauth_cache=True)
    video = yt.streams.filter(only_audio=True).first()

    # destination = '.'
    path_to_download =settings.MEDIA_ROOT+"/Downloads/"
    # print(path_to_download)
    out_file = video.download(output_path=path_to_download)
    base, ext = os.path.splitext(out_file)
    # print(base)
    new_file = base + '.mp3'
    # print(new_file)
    complete_path=out_file+new_file
    print("Hello")
    fileobj=Filedownloaded(filepath=str(new_file).split('/')[-1])
    fileobj.save()
    obj_id=fileobj.id
    fileobj=Filedownloaded.objects.get(id=obj_id)
    os.rename(out_file, new_file)
    return render(request=request,template_name='UMp3/downloaded.html',context={'fileobj':fileobj})
