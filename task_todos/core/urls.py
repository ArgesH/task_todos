from django.urls import path
from core.views import UploadImage

urlpatterns = [
    path('upload/', UploadImage.as_view(), name='upload_image'),
]
