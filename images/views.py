from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
# Create your views here.

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
