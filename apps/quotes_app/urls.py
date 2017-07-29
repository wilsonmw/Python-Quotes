from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^addQuote$', views.addQuote),
    url(r'^logout$', views.logout),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^addFavorite$', views.addFavorite),
    url(r'^removeFavorite$', views.removeFavorite),
]