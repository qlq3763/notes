from django.urls import path
from . import views

urlpatterns = [
    path('docs', views.DocListView.as_view(), name='docs'),
    path('doc/add', views.doc_add, name='doc-add'),
    path('doc/<slug>', views.doc_detail, name='doc-detail'),
    path('', views.DocListView.as_view(), name='docs'),
]
