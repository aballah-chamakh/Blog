from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Portfolio


def AboutView(request,*args,**kwargs):
    qs = Portfolio.objects.all()
    return render(request,'portfolio/about.html',{'objects':qs})


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'
