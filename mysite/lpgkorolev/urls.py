from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [path('', IndexView.as_view(), name='index'),
               path('about/', AboutView.as_view(), name='about'),
               path('service/', ServiceView.as_view(), name='service'),
               # path('appointment/', AppointmentCreate.as_view(), name='appointment'),
               path('price/', PriceView.as_view(), name='price'),
               # path('team/', TeamView.as_view(), name='team'),
               # path('reviews/', ReviewsView.as_view(), name='reviews'),
               path('contact/', ContactView.as_view(), name='contact'),
               path('about_lpg_massage/', AboutLPGView.as_view(), name='about_lpg_massage'),
               ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
