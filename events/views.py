from django.views import generic
from .models import EventCard


class EventList(generic.ListView):
    model = EventCard
    template_name = 'events/event.html'
