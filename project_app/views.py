from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Travel, Reys
from .forms import CreateTravelForm, UpdateTravelForm
from django.views.generic.edit import CreateView




def home(request):
    travels = Travel.objects.all()
    categories = Category.objects.all()
    reyslar = Reys.objects.all()
    return render(request, 'home.html',{'travels':travels, 'cats':categories, 'reyslar': reyslar})




def category(request, id):
    category = get_object_or_404(Category, id=id)
    travels = category.davlat.all().order_by('name')
    categories = Category.objects.all()
    reyslar = Reys.objects.all()
    return render(request, 'home.html', {'travels': travels, 'cats': categories, 'reyslar': reyslar})


def reys(request, id):
    reys = get_object_or_404(Reys, id=id)
    travels = reys.reys.all().order_by('name')
    categories = Category.objects.all()
    reyslar = Reys.objects.all()
    return render(request, 'home.html', {'travels': travels, 'reyslar': reyslar, 'cats': categories})



def batafsil(request,id):
    travel = get_object_or_404(Travel, id=id)
    return render(request,'batafsil.html',{'travel':travel})


# Create

def create_travel(request):
    form = CreateTravelForm()

    if request.method == 'POST':
        form = CreateTravelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    categories = Category.objects.all()
    reyslar = Reys.objects.all()
    return render(request, 'crud_travel.html',{'form':form, 'reyslar': reyslar, 'cats': categories})



# Update

def update_travel(request,id):
    travel = Travel.objects.get(id=id)
    if request.method == "POST":
        form = UpdateTravelForm(request.POST, instance=travel)
        if form.is_valid():
            form.save()
            return redirect('/')
        

    form = UpdateTravelForm(instance=travel)
    return render(request,'crud_travel.html',{'form':form})



# Delete 

def delete_travel(request, id):
    travel = Travel.objects.get(id=id)
    travel.delete()
    return redirect('/')

