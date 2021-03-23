from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('modelirovanie', views.modelirovanie, name='modelir'),
    path('news', views.news, name='news'),
    path('materials', views.materials, name='materials'),
    path('model/<slug:slug>', views.render_model_house),
    path('svoyamod', views.svoyafunk, name='svoya'),
    path("product/<slug:slug>", views.productfull, name="productfull"),
    path("news/<slug:slug>", views.newsfull, name="newsfull"),
    path('spasibo1', views.spasibo1, name="spasibo"),
    path('spasibo2', views.spasibo2, name="spasibo2"),
    path('product/<slug:slug>/zakaz', views.zakaz),
    path('materials/<slug:slug>', views.materialfull, name="materialfull"),
    path('kontakti', views.kontakti, name="kontakti"),

]