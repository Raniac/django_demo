from django.shortcuts import render, redirect
from django.http import HttpResponse
from web.models import Item, List

# Create your views here.
def home_page(request):
    # if request.method == 'POST':
    #     Item.objects.create(text=request.POST['item_text'])
    #     return redirect('/web/the-only-list-in-the-world/')
    
    # items = Item.objects.all()
    return render(request, 'home.html')
    # the third argument of render function is a dictionary
    # which maps template variable names to their values

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/web/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/web/{list_.id}/')