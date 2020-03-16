from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def test(request):
    #print(get_template())
    return render(request,"index.pug")
