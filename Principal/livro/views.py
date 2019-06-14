from django.shortcuts import render
from django.db import transaction
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from django.http import Http404, JsonResponse
from django.contrib import messages


from .models import Livro
from .forms import DependenteForm
from .forms import LivroForm, DependenteFormSet


class LivroListView(ListView):
    model = Livro
    template_name = 'livro/livro_list.html'


class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    success_url = 'livro:list'

    def get_context_data(self, **kwargs):
        context = super(LivroCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dependente_livro'] = DependenteFormSet(self.request.POST)
        else:
            context['dependente_livro'] = DependenteFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset_dependente = context['dependente_livro']

        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.save()

            if formset_dependente.is_valid():
                formset_dependente.instance = self.object
                formset_dependente.save()


        return super(LivroCreateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Não foi possível cadastrar')
        return super(LivroCreateView, self).form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, 'cadastrado com sucesso!!')
        return reverse(self.success_url)

class LivroUpdateView(UpdateView):
    model = Livro

    form_class = LivroForm
    success_url = 'livro:list'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        try:
            obj = Livro.objects.get(slug=slug)
        except:
            raise Http404("livro não localizado")
        return obj
    
    def get_context_data(self, **kwargs):
        context = super(LivroUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dependente_livro'] = DependenteFormSet(self.request.POST, instance=self.object)
        else:
            context['dependente_livro'] = DependenteFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset_dependente = context['dependente_livro']

        with transaction.atomic():
            self.object = form.save(commit=False)
            self.object.save()

            if formset_dependente.is_valid():
                formset_dependente.instance = self.object
                formset_dependente.save()
        return super(LivroUpdateView, self).form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, 'Não foi possível alterar')
        return super(LivroUpdateView, self).form_invalid(form)  

    def get_success_url(self):
        messages.success(self.request, 'Livro alterado com sucesso')
        return reverse(self.success_url)