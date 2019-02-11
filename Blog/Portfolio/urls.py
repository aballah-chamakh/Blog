from django.urls import path

from .views import PortfolioDetailView,AboutView

urlpatterns = [
    path('portfolio/<int:pk>/',PortfolioDetailView.as_view()),
    path('about/',AboutView),


]
