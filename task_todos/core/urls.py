from django.urls import path
from core.views import UploadImage, PhotoView

urlpatterns = [
    path('upload/', UploadImage.as_view(), name='upload_image'),
    path('upload_form/', PhotoView.as_view(), name='photo_view'),
]
