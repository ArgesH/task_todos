from django import forms
from core.models import Photo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'
        # self.helper.add_input(Submit('submit', 'Send Message'))
        # self.helper.add_input(Submit('submit', 'Submit'))


# class PhotoFormStatic(forms.Form):
#     title = forms.CharField(max_length=100)
#     image = forms.ImageField()