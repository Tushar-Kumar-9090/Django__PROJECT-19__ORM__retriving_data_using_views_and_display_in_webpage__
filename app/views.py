from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from app.models import *


## Inserting The Data Into Topic:-
def insert_topic(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse("<center><h3>Topic Data Is Inserted</h3></center>")


## Inserting The Data Into Webpages:-
def insert_webpage(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    n = input("Enter The Name: ")
    u = input("Enter The Url: ")
    WO = Webpage.objects.get_or_create(topic_name=TO, name=n, url=u)[0]
    WO.save()
    return HttpResponse("<center><h3>Webpage Data Inserted</h3></center>")


## Inserting The Data Into Access_records:-
def insert_access_records(request):
    tn = input("Enter The Topic_name: ")
    TO = Topic.objects.get_or_create(topic_name = tn)[0]
    TO.save()
    n = input("Enter The Name: ")
    WO = Webpage.objects.get_or_create(topic_name=TO, name=n, Url=u)[0]
    WO.save()
    d = input("Enter The Date: ")
    a = input("Enter The Author: ")
    ARO = AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    ARO.save()
    return HttpResponse("<center><h3>AccessRecord Data Inserted</h3></center>")


## -------------------------------------------------------------------------------------------------------------------



## Retrieving the data of Topic
def display_topics(request):

    topic=Topic.objects.all()
    d={'topics':topic}

    return render(request,'display_topics.html',d)


## Retrieving the data of Webpage
def display_webpages(request):

    webpage=Webpage.objects.all()
    d={'webpages':webpage}

    return render(request,'display_webpages.html',d)


## Retrieving the data of Access_records
def display_accessrecords(request):

    accessrecord=AccessRecord.objects.all()
    d={'accessrecords':accessrecord}

    return render(request,'display_access_records.html',d)













