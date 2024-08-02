from django import forms
from .models import Manual, Category

import re
from django.core.exceptions import ValidationError


class ManualForm(forms.ModelForm):
    class Meta:
        model = Manual
        fields = ['name', 'content', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'.*/|.*\\', name):
            raise ValidationError('Name must not begin with "/" or "\\"')
        return name


class ManualFileForm(forms.Form):

    # name = forms.CharField()
    file = forms.FileField(widget=forms.FileInput)
    category = forms.ChoiceField(
        choices=[(choice.pk, choice.title)
                 for choice in Category.objects.all()],
        label='Выберите вариант',
        required=True,
    )
