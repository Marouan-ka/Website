from django.urls import path
from django.conf.urls import handler404
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("portfolio/", views.work, name= "portfolio"),
    path("contact/", views.contact, name= "contact"),
    path("<slug:slug>/", views.portfoliopage, name= "portfoliopage"),
    # path("success/", views.success, name='success'),
]  
