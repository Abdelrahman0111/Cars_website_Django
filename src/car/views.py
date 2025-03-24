from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.



def home(request):
    return render(request, 'car/home.html')




def list(request):
    list = Car.objects.all()
    context = {'list': list}
    return render(request, 'car/list.html', context)


#
def add(request):
    if request.method == 'POST':
        make = request.POST['make']
        model = request.POST['model']
        year = request.POST['year']
        color = request.POST['color']
        price = request.POST['price']
        description = request.POST.get('description', '')
        image = request.FILES.get('image')
        
        car = Car.objects.create(
            make=make,
            model=model,
            year=year,
            color=color,
            price=price,
            description=description,
            image=image
        )
        messages.success(request, 'Car added successfully!')
        return redirect('list')
    else:
        return render(request, 'car/add.html')


def delete(request):
    if request.method == 'POST':
        car_id = request.POST.get('id')
        try:
            car = Car.objects.get(id=car_id)
            car.delete()
            messages.success(request, f'{car.make} {car.model} deleted successfully!')
        except Car.DoesNotExist:
            messages.error(request, 'Car not found!')
        return redirect('list')
    else:
        # Get unique values for filters
        make = request.GET.get('make', '')
        color = request.GET.get('color', '')
        
        # Query with filters
        cars = Car.objects.all()
        if make:
            cars = cars.filter(make=make)
        if color:
            cars = cars.filter(color=color)
            
        # Get unique values for dropdowns
        makes = Car.objects.values_list('make', flat=True).distinct()
        colors = Car.objects.values_list('color', flat=True).distinct()
        
        context = {
            'cars': cars,
            'makes': makes,
            'colors': colors,
            'selected_make': make,
            'selected_color': color,
        }
        return render(request, 'car/delete.html', context)