# Import base django dependencies
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.http import HttpResponse

# Auth to create sign up feature
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Import models
from .models import Event, Performer
from .forms import ScheduleForm

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = ['name', 'type', 'description', 'rating']

    # Interrupt normal form_valid functionality to assign user
    def form_valid(self, form):
        # Assign logged in user
        form.instance.user = self.request.user
        # Allow CreateView to continue
        return super().form_valid(form)

class EventDetail(LoginRequiredMixin, DetailView):
    model = Event

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = "/events"

class PerformersIndex(LoginRequiredMixin, ListView):
    model = Performer

class PerformersDetail(LoginRequiredMixin, DetailView):
    model = Performer

class PerformerCreate(LoginRequiredMixin, CreateView):
    model = Performer
    fields = '__all__'

class PerformerUpdate(LoginRequiredMixin, UpdateView):
    model = Performer
    fields = '__all__'

class PerformerDelete(LoginRequiredMixin, DeleteView):
    model = Performer
    success_url = '/performers'

# Define function view(s)
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1><a href="events/">Index</a>')

def about(request):
    return render(request, 'about.html')

@login_required
def events_index(request):
    events = Event.objects.filter(user=request.user)
    return render(
        request,
        'events/index.html',
        {'events':events}
    )

@login_required
def events_detail(request, event_id):
    event = Event.objects.get(id=event_id)

    schedule_form = ScheduleForm()

    performers_not_listed = Performer.objects.exclude(id__in = event.performers.all().values_list('id'))
     
    return render(
        request,
        'events/detail.html',
        {'event':event,
         'schedule_form': schedule_form,
         'performers': performers_not_listed,
        }
    )

@login_required
def add_schedule(request, event_id):
    form = ScheduleForm(request.POST)
    if form.is_valid():
        new_schedule = form.save(commit=False)
        new_schedule.event_id = event_id
        new_schedule.save()
    return redirect('detail', event_id = event_id)

@login_required
def assoc_performer(request, event_id, performer_id):
    Event.objects.get(id=event_id).performers.add(performer_id)
    return redirect('detail', event_id=event_id)

def signup(request):
    error_message = ''
    # Distinguish between page showing (GET) and submitting (POST)
    if request.method == 'POST':
        # Fill out the given django form with info from the page
        form = UserCreationForm(request.POST)
        # Save user to database
        if form.is_valid():
            user = form.save()
            # make sure the user stays signed IN upon sign UP
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # OR just show the page with an empty form to fill
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)