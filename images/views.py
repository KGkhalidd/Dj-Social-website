from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from .models import Image
# Create your views here.

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id , slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})

@login_required
def image_create(request):
    if request.method == 'POST':
        form= ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, 'Image saved successfully')
            return redirect(new_image.get_absolute_url()) # get_absolute not done yet
    else:
        form = ImageCreateForm(data=request.GET) #data=request.GET u can remove it
    return render(request, 'images/image/create.html', {'form':form})
