from django.views import generic
from .models import EventCard, Sponsors


class EventList(generic.ListView):
    model = EventCard
    template_name = 'events/event.html'


class SponsorsList(generic.ListView):
    model = Sponsors
    template_name = 'events/sponsors.html'
