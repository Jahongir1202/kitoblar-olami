from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, Jahon_adabiyotlar, Badiy, Bolalar, It, Diniy, Chettil


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    # fields = (  'photo')


class HomePageDetailView(DetailView):
    model = Post
    template_name = 'pages_detail.html'
class ItPageDetailView(DetailView):
    model = It
    template_name = 'pagesit_detail.html'
class JahonPageDetailView(DetailView):
    model = Jahon_adabiyotlar
    template_name = 'pagesjahon_detail.html'
class BadiyPageDetailView(DetailView):
    model = Badiy
    template_name = 'pagesbadiy_detail.html'
class BolalarPageDetailView(DetailView):
    model = Bolalar
    template_name = 'pagesbolalar_detail.html'
class ChetPageDetailView(DetailView):
    model = Chettil
    template_name = 'pageschet_detail.html'
class DinPageDetailView(DetailView):
    model = Diniy
    template_name = 'pagesdin_detail.html'
class AboutPageView(TemplateView):
    template_name = 'about.html'


class OnefPageView(ListView):
    model = Jahon_adabiyotlar
    template_name = 'onef.html'
    # fields = (  'photo')


class KebabsPageView(ListView):
    model = Bolalar
    template_name = 'kebabs.html'
    # fields = (  'photo')


class TwoPageView(ListView):
    model = Badiy
    template_name = 'twof.html'
    # fields = (  'photo')


class WaterPageView(ListView):
    model = Diniy
    template_name = 'water.html'
    # fields = (  'photo')


class ItPageView(ListView):
    model = It
    template_name = 'it.html'
    # fields = (  'photo')


class ChettilPageView(ListView):
    model = Chettil
    template_name = 'chettil.html'
    # fields = (  'photo')
# Create your views here.
