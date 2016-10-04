from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Person, ExecMember, Membership, Constitution, News, Event, Gallery
from .forms import MemberForm, ExeCommMemberForm, ConstitutionForm, MembershipForm, NewsForm, EventForm, GalleryFormSet

from user.decorators import require_authenticated_permission
from .utils import (FormsetMixin, PostFormValidMixin)

class HomePageView(TemplateView):

    template_name = 'member/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['gallery_list'] = Gallery.objects.order_by('-pub_date')[:4]
        return context

class MemberDetailView(generic.DetailView):
    model = Person
    template_name = 'member/member_detail.html'



class AlbumCreate(CreateView):
    model = Person
    fields = '__all__'

class AllMemberListView(generic.ListView):
    model = Person
    paginate_by = 10
    context_object_name = 'persons'

class GeneralMemberView(generic.ListView):
    model = Person
    paginate_by = 10
    context_object_name = 'persons'

    def get_queryset(self):
        queryset = super(GeneralMemberView, self).get_queryset()
        # queryset = queryset.filter(user=self.request.user)
        queryset = queryset.filter(category__id="1")
        return queryset

    #
class LifeMemberView(generic.ListView):
    model = Person

    paginate_by = 10
    context_object_name = 'persons'

    def get_queryset(self):
        queryset = super(LifeMemberView, self).get_queryset()
        # queryset = queryset.filter(user=self.request.user)
        queryset = queryset.filter(category__id="3")
        return queryset

@require_authenticated_permission(
'member.add_person')
class PersonCreate(PostFormValidMixin, CreateView):
    template_name = 'member/person_form.html'
    model = Person
    success_url = '/person/'
    form_class = MemberForm

@require_authenticated_permission(
'member.change_person')
class PersonUpdate(PostFormValidMixin, UpdateView):
    template_name = 'member/person_form.html'
    model = Person
    success_url = '/person/'
    form_class = MemberForm

@require_authenticated_permission(
'member.delete_person')
class PersonDelete(DeleteView):
    model = Person
    success_url = '/person/'

class ExeCommListView(generic.ListView):
    model = ExecMember
    context_object_name = 'members'


class ExeCommMembCreate(CreateView):
    template_name = 'member/execmember_form.html'
    model = ExecMember
    success_url = '/execomember/'
    form_class = ExeCommMemberForm

    def get_form(self):
        kwargs = super(ExeCommMembCreate, self).get_form()
        return kwargs


# Member Category

class MembershipView(generic.ListView):
    model = Membership
    context_object_name = 'entries'

@require_authenticated_permission(
'member.add_membership')
class MemberCatCreate(CreateView):
    template_name = 'member/membership_form.html'
    model = Membership
    success_url = '/membercat/'
    form_class = MembershipForm

#Constitution

class ConstitutionView(generic.ListView):
    model = Constitution
    context_object_name = 'documents'

@require_authenticated_permission(
'member.add_constitution')
class ConstitutionCreate(CreateView):
    template_name = 'member/constitution_form.html'
    model = Constitution
    success_url = '/cons/'
    form_class = ConstitutionForm

@require_authenticated_permission(
'member.delete_constitution')
class ConstitutionDelete(DeleteView):
    model = Constitution
    success_url = '/cons/'

@require_authenticated_permission(
'member.change_constitution')
class ConstitutionUpdate(UpdateView):
    template_name = 'member/constitution_form.html'
    model = Constitution
    success_url = '/cons/'
    form_class = ConstitutionForm



# News

class NewsListView(generic.ListView):
    model = News
    context_object_name = 'news_list'

@require_authenticated_permission(
'member.add_news')
class NewsCreate(CreateView):
    template_name = 'member/news_form.html'
    model = News
    success_url = '/news/'
    form_class = NewsForm

class NewsDetailView(generic.DetailView):

    model = News

@require_authenticated_permission(
'member.change_news')
class NewsUpdate(UpdateView):
    template_name = 'member/news_form.html'
    model = News
    success_url = '/news/'
    form_class = NewsForm

@require_authenticated_permission(
'member.delete_news')
class NewsDelete(DeleteView):
    model = News
    success_url = '/news/'


# Event and Gallery
@require_authenticated_permission(
'member.add_event')
class EventCreateView(FormsetMixin, CreateView):
    template_name = 'member/event_and_gallery_form.html'
    model = Event
    form_class = EventForm
    formset_class = GalleryFormSet

@require_authenticated_permission(
'member.change_event')
class EventUpdateView(FormsetMixin, UpdateView):
    template_name = 'member/event_and_gallery_form.html'
    is_update_view = True
    model = Event
    form_class = EventForm
    formset_class = GalleryFormSet


class GalleryList(generic.ListView):

    model = Gallery


class GalleryDetailView(generic.DetailView):

    model = Gallery


class EventList(generic.ListView):

    model = Event


class EventDetailView(generic.DetailView):

    model = Event

class EventGalleryListView(generic.ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'member/event_gallery.html'

@require_authenticated_permission(
'member.delete_event')
class EventDelete(DeleteView):

    model = Event
    success_url = '/event/'

class GalleryAllList(generic.ListView):

    model = Gallery
    context_object_name = 'object_list'
    template_name = 'member/gallery_all.html'

#Contact form

import operator

from django.db.models import Q
from functools import reduce
from itertools import chain
from operator import attrgetter


# ascending oreder

class SearchListView(generic.ListView):
    """
    Display a Blog List page filtered by the search query.
    """
    paginate_by = 10

    queryset = Gallery.objects.all()

    def get_queryset(self):
        result = super(SearchListView, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()

            q = Q()
            for query in query_list:
                q = (q & (Q(event__name__icontains=query) |
                          Q(event__description__icontains=query) |
                          Q(title__icontains=query)
                          ))
            return Gallery.objects.filter(q)


from django.conf import settings
from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', settings.EMAIL_HOST_USER,
         ['to@example.com'], fail_silently=False)

