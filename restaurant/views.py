# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

# Add your code here to create new views
def menu(request):
    menu_data = Menu.objects.all()
    return render(request, 'menu.html', {'menu_data': menu_data})

def display_menu_item(request, pk=None):
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, "menu_item.html", {'menu_item': menu_item})