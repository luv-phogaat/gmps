from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('admission', views.admission, name='admission'),
    path('career', views.career, name='career'),
    path('result', views.result, name='result'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   