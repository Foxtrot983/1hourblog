from django.urls import path
from .views import index, one

urlpatterns = [
    path('', index, name='main' ),
    path(r'<int:pk>', one, name='oneArticle')
]