from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Doc


class DocListView(ListView):
    """
    List all documents.
    """
    template_name = 'doc-list.html'
    queryset = Doc.objects.all()
    context_object_name = 'docs'


class DocContentView(DetailView):
    template_name = 'doc-content.html'
    model = Doc
    slug_field = 'slug'

