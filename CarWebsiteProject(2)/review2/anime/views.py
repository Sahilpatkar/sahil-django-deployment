from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .models import Car_Info
from .models import Review
from .forms import ReviewForm
from .forms import FormName
from .forms import FormName2

from django.contrib.auth import authenticate, login
from django.http import HttpResponse
def index(request):
    reviews = Review.objects.order_by('-date_added')

    context = {'reviews' : reviews}

    return render(request, 'anime/index.html', context)


def sign(request):
    if request.method == 'POST':
        print("here1")
        form = ReviewForm(request.POST)
        user = request.user
        if form.is_valid():
            new_review = Review(name=request.POST['name'] + "- " + user.username ,review = request.POST['review'])
            new_review.save()
            print("review form saved")
            return redirect('index')

    else:
        form = ReviewForm()

    context = {'form' : form}
    return render(request, 'anime/sign.html',context)
                

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request,user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html',context)

def car(request):
    form2 = FormName()
    
    req_car = "NONE"
    req_car2 = "NONE"
    
    if request.method == 'POST':
        form2 = FormName(request.POST)

        if form2.is_valid():
            print("val_SUCCESS")
            print("CAR_NAME: "+form2.cleaned_data["category"])
            req_car = form2.cleaned_data["category"]
            req_car2 = form2.cleaned_data["category2"]


    return render(request, 'anime/CarComp.html',
     {"form2":form2,'Car_Info': Car_Info.objects.get(CarName=req_car),
     'Car_Info2': Car_Info.objects.get(CarName=req_car2)})



