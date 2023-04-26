# Import base django dependencies
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

# Import models
from .models import Event
from .forms import ScheduleForm

# Define class view(s)
# class CollectionList(ListView):
#     model = Item
#     template_name = 'index.html'

class EventCreate(CreateView):
    model = Event
    fields = '__all__'

class EventDetail(DetailView):
    model = Event

class EventUpdate(UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(DeleteView):
    model = Event
    success_url = "/events"

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

    schedule_form = ScheduleForm()
     
    return render(
        request,
        'events/detail.html',
        {'event':event,
         'schedule_form': schedule_form
        }
    )

def add_schedule(request, event_id):
    form = ScheduleForm(request.POST)
    if form.is_valid():
        new_schedule = form.save(commit=False)
        new_schedule.event_id = event_id
        new_schedule.save()
    return redirect('detail', event_id = event_id)