from django.conf.urls import url
from blog_app import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog import settings

urlpatterns =[
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^home/$',views.TripListView.as_view(),name='trip_list'),
    #url(r'^$',views.ImageView.as_view(),name='image_view'),
    # matching the primary key to whatever you clicked on:
    url(r'^accounts/update/(?P<pk>[\-\w]+)/$',views.edit_user,name='update_account'),
    url(r'^trip/(?P<pk>\d+)$',views.TripDetailView.as_view(),name='trip_detail'),
    url(r'^trip/new/$',views.CreateTripView.as_view(),name='trip_new'),
    url(r'^trip/(?P<pk>\d+)/edit/$',views.TripUpdateView.as_view(),name='trip_edit'),
    url(r'^trip/(?P<pk>\d+)/remove/$',views.TripDeleteView.as_view(),name='trip_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='trip_draft_list'),
    url(r'^trip/(?P<pk>\d+)/comment/$',views.AddCommentToTrip.as_view(),name='AddCommentToTrip'),
    url(r'^comment/(?P<pk>\d+)/edit',views.CommentUpdateView.as_view(),name='comment_edit'),
    url(r'^comment/(?P<pk>\d+)/remove',views.comment_remove,name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/approve',views.comment_approve,name='comment_approve'),
    url(r'^trip/(?P<pk>\d+)/publish',views.trip_publish,name='trip_publish'),
    url(r'^register/$',views.register,name='register'),
    #url(r'^login/$',views.user_login,name='login'),
    url(r'profile/(?P<pk>\d+)$', views.get_user_profile, name ='get_user_profile'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+= staticfiles_urlpatterns()
