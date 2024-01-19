from django.shortcuts import render, redirect
from .forms import HotelForm
from django.contrib import messages
from .models import Hotels


def add_hotel(request):
    template = 'app1/add_hotel.html'
    form = HotelForm()
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Hotel added Successfully!')
            return redirect('show_url')
    context = {"form": form}
    return render(request, template, context)

def show_hotels(request):
    template = 'app1/show_hotels.html'
    hotels = Hotels.objects.order_by('-id')
    context = {"hotels": hotels}
    return render(request, template, context)

