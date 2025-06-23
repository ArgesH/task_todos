from django.shortcuts import render, redirect
from django.views import View
from core.models import Photo

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
