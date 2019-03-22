from django.urls import path
from . import views

urlpatterns = [
    path('docs', views.DocListView.as_view(), name='docs'),
    path('doc/<slug>', views.DocContentView.as_view(), name='content'),
    path('', views.DocListView.as_view(), name='docs'),
]
