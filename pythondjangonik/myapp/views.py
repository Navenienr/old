from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def index (request):
    return render (request, "index.html")

def about (request):
    return render (request, "about.html")

def contacts (request):
    return render (request, "contacts.html")

def forms (request):
    return render (request, "forms.html")

def postuser(request):
    Login = request.POST.get("Login", "Undefined")
    Password = request.POST.get("Password", )
    return HttpResponse(f"<h2>Login: {Login}  Password:{Password}" )




# получаем все объекты
people = Person.objects.all()
print(people.query)
 
# получаем объекты с именем Tom
people = people.filter(Login = "Tom")
print(people.query)
 
# получаем объекты с возрастом, равным 31
people = people.filter(Password = 31)
print(people.query)
 
# здесь происходит выполнения запроса в БД
for person in people:
    print(f"{person.id}.{person.Login} - {person.Password}")