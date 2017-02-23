from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^queryBrands/$',views.queryBrands,name='queryBrands'),
    url(r'^queryBrandCategory/$', views.queryBrandCategory, name='queryBrands'),
    url(r'^$', views.index, name='index')
               ]