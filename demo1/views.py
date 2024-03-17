from django.shortcuts import render, HttpResponse



def get1(request):
    msg = 'i am here'
    return HttpResponse(msg)