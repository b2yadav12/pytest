from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from resp.models import Person

def html(request):
    response = HttpResponse()
    response.write("<h2><center>Welcome To Django!</center></h2>")
    return response

def json(request):
    return JsonResponse({'foo': 'bar'})

def createPerson(request):
    person=Person(first_name='Amit', last_name='Singh')
    person.save()

    response = HttpResponse()
    response.write("<h2><center>New Person Saved Succeessfully</center></h2>")
    return response

def personList(request):
    persons=Person.objects.all()
    print("Person List Start")

    for row in persons:
        print(str(row.id)  + " : " + row.first_name + " " + row.last_name)

    print("Person List End")
    response = HttpResponse()
    response.write("<h2><center>Querysets are printed in terminal</center></h2>")
    return response

def filterPersion(request, first_name):
    print("param : " + first_name)
    persons=Person.objects.filter(first_name=first_name).all()
    print("Person List Start")

    for row in persons:
        print(str(row.id)  + " : " + row.first_name + " " + row.last_name)

    print("Person List End")
    response = HttpResponse()
    response.write("<h2><center>Querysets are printed in terminal</center></h2>")
    return response

def getPersion(request, id):
    person=Person.objects.get(id=id)
    print("Person row start")

    print(str(person.id)  + " : " + person.first_name + " " + person.last_name)

    print("Person row End")
    response = HttpResponse()
    response.write("<h2><center>Person details are printed in terminal</center></h2>")
    return response