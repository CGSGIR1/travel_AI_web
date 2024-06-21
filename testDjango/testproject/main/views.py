from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def addinfo(request):
    return render(request, 'main/addinfo.html')
