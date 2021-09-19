from os import name
from django.shortcuts import render
from .models import Images
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def index(request):
    template = 'pic/home.html'
    context = {}
    return render(request,template,context)

def success(request):
    template = 'pic/success.html'
    if request.method == 'POST':
        images = request.FILES.getlist('images')
        for i in images:
            img_obj = Images(image=i)
            img_obj.save()
            
    images = Images.objects.all().order_by('-date_posted')
    
    paginator = Paginator(images, 1)
    page_number = request.GET.get('page')

    for key, value in request.GET.items():
        if key != 'page':
            name_obj = Images.objects.get(image=f"{key}") 
            name_obj.image_name = value
            print('name:',key,'\n value:',value)
            name_obj.save()

    page_obj = paginator.get_page(page_number)
    context = {
            'page_obj':page_obj,
            'length': len(images)
        }

    return render(request,template,context)
