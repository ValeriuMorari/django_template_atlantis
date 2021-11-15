# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from .forms import HilForm, TestCaseForm, HILsModalForm
from .models import HilModel
from .tables import HILsTable
from django.views import View
from django_tables2 import SingleTableView
from django.shortcuts import redirect
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


class HilsView(SingleTableView):
    SingleTableView.table_pagination = False
    model = HilModel
    table_class = HILsTable
    template_name = 'home/hils.html'


class TestCaseManager(View):

    @staticmethod
    def get(request):
        form = TestCaseForm()
        return render(request, 'home/p_forms.html', {
            'form': form,
            'form_title': str(TestCaseForm()),
        })

    @staticmethod
    def post(request):
        form = TestCaseForm(request.POST)
        if form.is_valid():
            form.save()
            note = 'success'
        else:
            note = 'Form is not valid'
        return render(request, 'home/p_forms.html', {
            'form': form,
            'form_title': str(TestCaseForm()),
            'note': note
        })


class HilManager(ContextMixin, View):

    @staticmethod
    def get(request):
        form = HilForm()
        return render(request, 'home/p_forms.html', {
            'form': form,
            'form_title': str(HilForm())
        })

    @staticmethod
    def post(request):
        form = HilForm(request.POST)
        note = str()
        if form.is_valid():
            form.save()
            note = 'Form is not valid; you are too good'
        else:
            note = 'Form is not valid'
        return render(request, 'home/p_forms.html', {
            'form': form,
            'form_title': str(HilForm()),
            'note': note
        })


class HilManagerModal(BSModalCreateView):
    template_name = 'layouts/modal_create.html'
    form_class = HILsModalForm
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('hils')


def delete(request, hil_id):
    HilModel.objects.filter(id=hil_id).delete()
    return redirect('hils')
