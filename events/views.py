from django.views import generic
from .models import EventCard, Sponsors
from .forms import EventForm
from django.shortcuts import redirect, render
from django.http import HttpResponse


def event_reg(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204)
    else:
        form = EventForm()
    return redirect('/events/') 


class EventList(generic.ListView):
    model = EventCard
    template_name = 'events/event.html'
    context_object_name = "eventcard_list"


class SponsorsList(generic.ListView):
    model = Sponsors
    template_name = 'events/sponsors.html'
