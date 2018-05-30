from django.conf.urls import url
from booktest import views
urlpatterns = [
    url(r'^show_area(?P<pindex>\d*)$',views.show_area),
    url(r'^areas$',views.areas),
    url(r'^prov$',views.prov),
    url(r'^city(\d+)$',views.city),
    url(r'^dis(\d+)$',views.dis),
]