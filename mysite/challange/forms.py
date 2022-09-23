from django.forms import ModelForm
from challange.models import Name


# Create the form class.
class NameForm(ModelForm):
    class Meta:
        model = Name
        fields = '__all__'
