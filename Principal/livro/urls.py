from django.urls import path

from .views import LivroCreateView
from .views import LivroListView, LivroUpdateView

app_name = 'livro'
urlpatterns = [
    path('', LivroCreateView.as_view(), name="create"),
    path('listar/', LivroListView.as_view(), name="list"),
    path('alterar/<slug:slug>/', LivroUpdateView.as_view(), name="update"),
    
]