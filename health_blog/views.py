from django.shortcuts import render


def index(request):
    return render(request,"hikmet.html")

def deneme(request):
    return render(request,"karamel.html")