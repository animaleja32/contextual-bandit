from django.conf.urls import url

from . import views

app_name = 'artrecommender'
urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^joy$', views.joy, name='joy'),
    url(r'^black_panther$', views.black_panther, name='black_panther'),
    url(r'^pj_masks$', views.pj_masks, name='pj_masks'),
]
