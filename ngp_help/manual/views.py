from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from typing import Any
from django.db.models.query import QuerySet

from markdown_it import MarkdownIt

from .models import Manual


class ManualListView(ListView):
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


# class ManualDetailView(DetailView):

#     model = Manual
#     context_object_name = 'manual_item'

# def manual_detail_view(request, pk):
#     md = markdown.Markdown(extensions=['markdown.extensions.tables'])
#     manual = Manual.objects.get(id=pk)
#     manual.content = md.convert(manual.content)
#     context = {
#         'manual_item': manual,
#     }
#     return render(request=request, template_name='manual/manual_detail.html', context=context)
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
