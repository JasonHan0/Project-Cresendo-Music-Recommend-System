from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.

class index(generic.ListView):
    def __init__(self):
        self.title_nm       = "메인"
        self.ogImgUrl       = ""
        self.descript       = "메인"
        self.template_name  = "main/index.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,
                        "dataList":"[[[[ Hellow DJango ]]]]"}

        return render(request, self.template_name, self.content)


class firstIndex(generic.ListView):
    def __init__(self):
        self.title_nm       = "main에 오신것을 환영합니다. "
        self.ogImgUrl       = ""
        self.descript       = ""
        self.template_name  = "index.html"

    def get(self, request, *args, **kwargs):
        self.content = {"descript":self.descript,
                        "title_nm":self.title_nm,
                        "ogImgUrl":self.ogImgUrl,
                        "dataList":""}

        return render(request, self.template_name, self.content)

