from django.conf.urls import url
from resources import views

urlpatterns = [
        # url(r'^$',
        #     views.ResourceList.as_view(),
        #     name='resources_list'),

        # url(r'^(?P<pk>[0-9]+)/$',
        #     views.ResourceDetail.as_view(),
        #     name='resources_detail'),

        # url(r'^create/$',
        #     views.ResourceCreate.as_view(),
        #     name='resources_create'),

        # url(r'^(?P<pk>[0-9]+)/update/$',
        #     views.ResourceUpdate.as_view(),
        #     name='resources_update'),

        # url(r'^(?P<pk>[0-9]+)/delete/$',
        #     views.ResourceDelete.as_view(),
        #     name='resources_delete'),
        url(r'^create', views.ResourceCreate.as_view(), name='resources_create')
]
