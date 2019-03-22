from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Doc


class DocListView(ListView):
    """
    List all documents.
    """
    template_name = 'doc-list.html'
    queryset = Doc.objects.all()
    context_object_name = 'docs'


def doc_detail(request, slug):
    doc = get_object_or_404(Doc, slug=slug)
    old_slug = doc.slug

    if request.method == 'POST':
        doc.title = request.POST['title'].strip()
        doc.content = request.POST['content'].strip()
        doc.save()

    if old_slug == doc.slug:
        return render(request, 'doc-detail.html', {'doc': doc})
    else:
        return HttpResponseRedirect(reverse('docs'))


def doc_add(request):
    if request.method == 'GET':
        return render(request, 'doc-add.html')
    else:
        doc = Doc.objects.create(title=request.POST['title'].strip(),
                                 content=request.POST['content'].strip())

        return HttpResponseRedirect(reverse('docs'))


