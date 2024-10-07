# from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from .models import Appointment
from .forms import AppointmentForm
from django.views.generic import CreateView, TemplateView


class IndexView(TemplateView):
    template_name = 'lpgkorolev/index.html'


class AboutView(TemplateView):
    template_name = 'lpgkorolev/about.html'


class ServiceView(TemplateView):
    template_name = 'lpgkorolev/service.html'


class PriceView(TemplateView):
    template_name = 'lpgkorolev/price.html'


class TeamView(TemplateView):
    template_name = 'lpgkorolev/team.html'


class ReviewsView(TemplateView):
    template_name = 'lpgkorolev/reviews.html'


class ContactView(TemplateView):
    template_name = 'lpgkorolev/contact.html'


class AboutLPGView(TemplateView):
    template_name = 'lpgkorolev/cont_lpg.html'


class AppointmentCreate(CreateView):
    form_class = AppointmentForm
    template_name = 'lpgkorolev/appointment_form.html'

    # success_url = reverse_lazy('appointment')

    def get_success_url(self):
        return reverse('appointment')
