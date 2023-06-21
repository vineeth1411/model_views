from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    tn =  input("enter topic name : ")
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    return HttpResponse("Topic is inserted")

def insert_webpage(request):
    to =  input("enter topic name : ")
    TO = Topic.objects.get_or_create(topic_name = to)[0]
    TO.save()
    n = input("enter name : ")
    u = input("enter url : ")
    WO = WebPage.objects.get_or_create(topic_name = TO , name = n , url = u)[0]
    WO.save()
    return HttpResponse("WebPage is created")
def insert_accessrecord(request):
    t = input("enter topic name : ")
    TO = Topic.objects.get_or_create(topic_name=t)[0]
    TO.save()
    N = input("enter Name : ")
    U = input("enter Url : ")
    D = input("Enter Date : ")
    Au = input("Enter Author Name : ")
    WO = WebPage.objects.get_or_create(topic_name = TO,name = N, url = U)[0]
    WO.save()
    AO = AccessRecord.objects.get_or_create(name = WO , date = D, author = Au)[0]
    AO.save()
    return HttpResponse("Access Record Created")
