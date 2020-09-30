#Installing Django to our directory

# install django (pip install Django)

#to make new project (django-admin startproject project_name)

#to start the server (python manage.py runserver) manage.py helps us using command in our django app, click on the ip adress to check if weverything works successfully

#to create new app (python manage.py startapp hello)

#now we need to install our new app inside django so we go to settings.py and then we add "project name" inside 'installed apps'

#now go to views.py inside our new created app , consider it the place you want to view to the user\


#!--------------------
#we need to print hello when the user enters the website but first we need to get the
#http request and then respond

#to send respond we need to import a library
from django.http import HttpResponse

def index(request): #the parameter is http requesnt
    return HttpResponse("Hello, World") #the way we respond


#now we need to tell the function what url when visited should we respond so we will create a new file for urls in our app 'urls.py'
 #? *inside urls.py

#we first need to import path module to add the url then make a list with all possible urls

from django.urls import path
from . import views  #the '.' means current directory and views is the file with the  function

url_patterns= [
    path("",views.index,name="index") #first parameter is the url "" means default, second is the function to be excuted when url is visited, third is optional and is specifying name to our url
] #first parameter is the url "" means default, second is the function to be excuted when url is visited, third is optional and is specifying name to our url
]

#now in our main project's urls.py we will add our hello urls to the main app urls
#inside urlpatterns array add our array
path('hello/',include("hello.urls"))
#in the import of this urls.py add "include, " before path


#now we can visit our site using "python manage.py runserver"
#copying the id_address:port/hello


#if we want to add another url we will repeat
def Mustafa(request):
    return HttpResponse("Hello, Mustafa")

#? inside hello urls.py
url_patterns= [
        path("",views.index,name="index"),
        path("Mustafa",views.Mustafa,name="Mustafa")
]

#now to visit it "python manage.py runserver" then entering the url id_address:port/hello/Mustafa