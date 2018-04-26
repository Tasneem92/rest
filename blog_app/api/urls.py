from django.conf.urls import url
from blog_app.api import views
from django.contrib import admin

urlpatterns = [
    url(r'^$',views.TripListAPIView.as_view(),name='list'),
    # matching the primary key to whatever you clicked on:
    url(r'^(?P<pk>\d+)/$',views.TripDetailAPIView.as_view(),name='detail'),
    url(r'^create/$',views.TripCreateAPIView.as_view(),name='create'),
    url(r'^(?P<pk>\d+)/edit/$',views.TripUpdateAPIView.as_view(),name='edit'),
    url(r'^(?P<pk>\d+)/remove/$',views.TripDeleteAPIView.as_view(),name='remove'),
    #url(r'^drafts/$',views.DraftListView.as_view(),name='trip_draft_list'),
    #url(r'^trip/(?P<pk>\d+)/comment/$',views.add_comment_to_trip,name='add_comment_to_trip'),
    #url(r'^comment/(?P<pk>\d+)/approve',views.comment_approve,name='comment_approve'),
    #url(r'^comment/(?P<pk>\d+)/remove',views.comment_remove,name='comment_remove'),
    #url(r'^trip/(?P<pk>\d+)/publish',views.trip_publish,name='trip_publish'),
    #url(r'^register/$',views.register,name='register'),
]
