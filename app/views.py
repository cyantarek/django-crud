from django.shortcuts import render, redirect
from app.models import Dog

# Create your views here.
def index(request):
    dogs = Dog.objects.all()
    context = {
        "dogs": dogs
    }
    return render(request, "index.html", context)

def create(request):
    dog = Dog(name=request.POST["name"], breed=request.POST["breed"])
    dog.save()
    return redirect("/")

def edit(request, id):
    dog = Dog.objects.get(id=id)
    context = {
        "dog": dog
    }
    return render(request, "edit.html", context)

def update(request, id):
    dog = Dog.objects.get(id=id)
    dog.name = request.POST["name"]
    dog.breed = request.POST["breed"]
    dog.save()

    return redirect("/")

def delete(request, id):
    dog = Dog.objects.get(id=id)
    dog.delete()

    return redirect("/")