from django.forms import ModelForm
from .models import Request

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = "__all__"

