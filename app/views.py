from django.shortcuts import render


def Indexpage(req):
    return render (req, "app/index.html")