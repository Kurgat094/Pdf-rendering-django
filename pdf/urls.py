from django.urls import path
from .views import render_pdf_view


urlspatterns = [
    path('', render_pdf_view,  name='generate_pdf'),
]