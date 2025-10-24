from django.forms import ModelForm
from .models import Contact


class ContactForm(ModelForm):
    class Meta: 
        model = Contact
        fields = '__all__'


         # name = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=254)
    # mob = forms.CharField(max_length=20)
    # message = forms.TextField()
