from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
# from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return HttpResponse("<h4>Hello</h4>")


def about(request):
    return HttpResponse('<h1>Наш клуб</h1>')


# RETRIEVE
def home(request):
    # Retrieve all the persons' datas.
    get_persons = CustomUser.objects.all()
    params = {'people': get_persons}
    return render(request, 'mainApp/home.html', params)


# CREATE
def add_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')  # Эти поля существуют в базовой модели джанго из коробки, поэтому я не создал их вручную в модели
        email = request.POST.get('email')
        password = request.POST.get('password')

        create_person = CustomUser.objects.create_user(username=username, email=email, password=password)
        create_person.save()
        return redirect('/')
    else:
        return HttpResponse('GET request is not allowed.')


# UPDATE
def update_user(request, id):
    try:
        user = CustomUser.objects.get(id=id)

        if request.method == "POST":
            user.username = request.POST.get("username")
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.save()
            return redirect('/')
        else:
            return render(request, "mainApp/update.html", {"user": user})
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# DELETE
def delete_user(request, id):
    try:
        person = CustomUser.objects.get(id=id)
        person.delete()
        return redirect('/')
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")
