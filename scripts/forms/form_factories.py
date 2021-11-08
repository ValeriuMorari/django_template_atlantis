from __future__ import annotations
from django import forms
from django.forms import modelform_factory


class AtlantisModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AtlantisModelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


def model_form_creator(model_, theme: str) -> forms.ModelForm:
    """
    Factory function used to get specific theme form.
    :param theme: used theme e.g. Atlantis
    :param model_: model from models.py
    :return: form instance if theme was found else default form instance is returned
    """
    themes = {
        'atlantis': AtlantisModelForm
    }
    return modelform_factory(model=model_, form=themes.get(theme, forms.ModelForm), fields='__all__')
