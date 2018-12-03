from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
    # the third argument of render function is a dictionary
    # which maps template variable names to their values