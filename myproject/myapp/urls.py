from django.urls import path
from . import views
from .views import add_author, add_quote

app_name = 'myapp'

urlpatterns = [

    path('', views.all_quotes, name='quotes'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', add_author, name='add_author'),
    path('add_quote/', add_quote, name='add_quote'),

]
