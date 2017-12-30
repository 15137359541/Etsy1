from django.conf.urls import url
from . import views

app_name = 'platformes'

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
url(r'^file_update/$',views.file_update,name='file_update'),
url(r'^tatalGoods/$',views.tatalGoods,name='tatalGoods'),
]