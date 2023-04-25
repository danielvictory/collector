# Import base django dependencies
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse

# Import models
from .models import Event

# Define class view(s)
# class CollectionList(ListView):
#     model = Item
#     template_name = 'index.html'

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventDetail(DetailView):
    model = Event


# Define function view(s)
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1><a href="events/">Index</a>')

def about(request):
    return render(request, 'about.html')

def events_index(request):
    events = Event.objects.all()
    return render(
        request,
        'events/index.html',
        {'events':events}
    )

def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(
        request,
        'events/detail.html',
        {'event':event,}
    )