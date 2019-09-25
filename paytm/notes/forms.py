from django.forms import ModelForm, HiddenInput
from .validators import max_notes_validator
from .models import notes


class NotesForm(ModelForm):
    class Meta:
        model = notes
        fields = ['title', 'notes_desc']
        # fields = '__all__'
        # widgets = {
        #     'User': HiddenInput
        # }

    # def clean(self):
    #     cleaned_data = super(NotesForm, self).clean()
    #     print(cleaned_data, "cleaned_data")
    #     # max_notes_validator(cleaned_data['user'], add=1)
    #     return cleaned_data