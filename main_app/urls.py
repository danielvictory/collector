from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('events/', views.events_index, name='index'),
    path('events/<int:event_id>', views.events_detail, name='detail'),

    path('events/create', views.EventCreate.as_view(), name="events_create"),
    path('events/<int:pk>/update', views.EventUpdate.as_view(), name="events_update"),
    path('events/<int:pk>/delete', views.EventDelete.as_view(), name="events_delete"),

    path('events/<int:event_id>/add_schedule', views.add_schedule, name='add_schedule'),

    path('performers/', views.PerformersIndex.as_view(), name='performers_index'),
    path('performers/<int:pk>/', views.PerformersDetail.as_view(), name='performer_detail'),
    path('performers/create', views.PerformerCreate.as_view(), name='performers_create'),
    path('performers/<int:pk>/update', views.PerformerUpdate.as_view(), name='performer_update'),
    path('performers/<int:pk>/delete', views.PerformerDelete.as_view(), name='performer_delete'),

    path('events/<int:event_id>/assoc_performer/<int:performer_id>', views.assoc_performer, name='assoc_performer'),

    path('accounts/signup', views.signup, name='signup'),
]