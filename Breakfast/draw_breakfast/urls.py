from django.conf.urls import include, url
from .views import home,choosefood  # explicit relative import

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^choosefood/$', choosefood, name="choosefood"),

]