from django.conf.urls import url
from . import views

from .forms import MemberForm
from django import forms

app_name = 'member'
urlpatterns = [

    url(r'^$', views.HomePageView.as_view(), name='home'),

    # Member
    url(r'^(?P<pk>[0-9]+)/$', views.MemberDetailView.as_view(), name='member-detail'),
    url(r'member/add/$', views.AlbumCreate.as_view(), name='member-add'),
    url(r'^person/$', views.GeneralMemberView.as_view(), name='person-list'),
    url(r'^lifemember/$', views.LifeMemberView.as_view(), name='lifemember-list'),
    url(r'^person/create$', views.PersonCreate.as_view(), name='person-create'),
    url(r'^person/(?P<pk>[0-9]+)/update$', views.PersonUpdate.as_view(), name='person-update'),
    url(r'^person/(?P<pk>[0-9]+)/delete$', views.PersonDelete.as_view(), name='person-delete'),
    url(r'^allmember/$', views.AllMemberListView.as_view(), name='all-member'),

    # Executive Member
    url(r'^execomember/$', views.ExeCommListView.as_view(), name='execomember-list'),
    url(r'^execomember/create$', views.ExeCommMembCreate.as_view(), name='execomember-create'),

    # Member Category
    url(r'^membercat/$', views.MembershipView.as_view(), name='member-cat'),
    url(r'^membercat/create/$', views.MemberCatCreate.as_view(), name='membercat-create'),

    # Constitution
    url(r'^cons/$', views.ConstitutionView.as_view(), name='cons-list'),
    url(r'^cons/create/$', views.ConstitutionCreate.as_view(), name='cons-create'),
    url(r'^cons/(?P<pk>[0-9]+)/update$', views.ConstitutionUpdate.as_view(), name='cons-update'),
    url(r'^cons/(?P<pk>[0-9]+)/delete$', views.ConstitutionDelete.as_view(), name='cons-delete'),

    # News
    url(r'^news/$', views.NewsListView.as_view(), name='news-list'),
    url(r'^news/create/$', views.NewsCreate.as_view(), name='news-create'),
    url(r'^news/(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='news-detail'),
    url(r'^news/(?P<pk>[0-9]+)/update/$', views.NewsUpdate.as_view(), name='news-update'),
    url(r'^news/(?P<pk>[0-9]+)/delete/$', views.NewsDelete.as_view(), name='news-delete'),


    # Event and Gallery
    url(r'^gallery/$', views.GalleryList.as_view(), name='gallery-list'),
    url(r'^gallery/(?P<pk>\d+)/$', views.GalleryDetailView.as_view(), name='gallery-detail'),
    url(r'^event/$', views.EventList.as_view(), name='event-list'),
    url(r'^event/(?P<pk>\d+)/$', views.EventDetailView.as_view(), name='event-detail'),
    url(r'^event/gallery/$', views.EventGalleryListView.as_view(), name='event-gallery'),
    url(r'^event/create/$', views.EventCreateView.as_view(), name='create_event_and_gallery'),
    url(r'^event/(?P<pk>\d+)/update/$', views.EventUpdateView.as_view(), name='update_event_and_gallery'),
    url(r'^event/(?P<pk>[0-9]+)/delete/$', views.EventDelete.as_view(), name='event-delete'),
    url(r'^gallery/all/$', views.GalleryAllList.as_view(), name='gallery-all'),

    # Search

    url(r'^search/$', views.SearchListView.as_view(), name='search'),
   ]
