
from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import ugettext_lazy as _

from .models import Livro, Dependente

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ('slug',)


class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        exclude = ()



DependenteFormSet = inlineformset_factory(Livro, Dependente,
                                              fields=('nome_autor','email'),
                                              form=DependenteForm, extra=1)
