from django.shortcuts import render, redirect
from django.views import View
from core.models import Photo
from core.forms import PhotoForm

# Create your views here.

class UploadImage(View):
    def get(self, request):
        return render(request, 'upload.html', {"photos": Photo.objects.all()})
    
    def post(self, request):
        # 'image' matches the <input name="image" ...> in the form
        img = request.FILES.get('image')
        title = request.POST.get('title', 'base_image')
        if img:
            Photo.objects.create(title=title, image=img)
            return redirect('upload_image')


class PhotoView(View):
    def get(self, request):
        form = PhotoForm()
        return render(request, 'upload_form.html', {'form': form})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
        return render(request, 'upload_form.html', {'form': form})

