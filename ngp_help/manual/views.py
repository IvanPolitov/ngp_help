from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView, CreateView
from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadhandler import MemoryFileUploadHandler

from markdown_it import MarkdownIt

from .models import Manual, Category
from .forms import ManualForm, ManualFileForm


class ManualListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = ''

    model = Manual
    template_name = 'manual/manuals.html'
    context_object_name = 'manuals'
    # paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все руководства'
        return context

    def get_queryset(self) -> QuerySet[Any]:
        return Manual.objects.all().order_by('name')


@login_required(login_url='login', redirect_field_name='')
def manual_detail_view(request, pk):
    md = (
        MarkdownIt('commonmark', {'breaks': True,
                   'html': True}).enable('table')
    )
    manual = Manual.objects.get(id=pk)
    manual.content = md.render(manual.content)

    context = {
        'manual_item': manual,
    }
    return render(request=request, template_name='manual/manual_detail.html', context=context)


class CreateManual(LoginRequiredMixin, CreateView):

    form_class = ManualForm
    template_name = 'manual/manual_add.html'
    success_url = reverse_lazy('manuals')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_login_url(self) -> str:
        return 'login'

    def get_redirect_field_name(self) -> str:
        return ''


class CreateManualFromFile(LoginRequiredMixin, FormView):
    form_class = ManualFileForm
    template_name = 'manual/manual_add_file.html'
    success_url = reverse_lazy('manuals')

    def form_valid(self, form: Any) -> HttpResponse:
        data = form.cleaned_data
        file = data['file']
        content = ''
        with file.open('rb') as f:
            content = f.read().decode('utf-8')

        file_name = file.name[:-3]
        create_data = {
            'name': file_name,
            'content': content,
            'creator': self.request.user,
            'category': Category.objects.get(pk=data['category']),
        }
        instance = Manual.objects.create(**create_data)
        instance.save()

        return super().form_valid(form)

    def get_login_url(self) -> str:
        return 'login'

    def get_redirect_field_name(self) -> str:
        return ''
