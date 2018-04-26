from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog_app.models import Trip, AuthUser, Storycomment, Tripcomment, Userprofile
from django.contrib.auth.models import User
from blog_app.forms import TripForm, StoryForm, UserForm, TripCommentForm, StoryCommentForm, UserProfileForm
from django.urls import reverse_lazy # it waits until I delete the trip until it view the url
from django.http import HttpResponseRedirect, HttpResponse
 # zay el decorator ta3 el functions based view bas lal classes based view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.template import Template, Context
# Create your views here.
import datetime

class AboutView(TemplateView):
    template_name = 'about.html'

class ImageView(TemplateView):
    model = Userprofile


class TripListView(ListView):
    model = Trip

    # define how to grab trips list
    # queryset allows to me to use Django ORM when dealing with generic views
    # to add a custom touch to ORM
    # SQL query on my model that grabs the trip model objects and filter it based on my condition
    # date__lte: grabs date
    # and after __ you write the field condition
    # lte is a condition : less than or equal to
    # date : the dash (-) orders them in descending order, the most recent blog trips comes up front
    def get_queryset(self):
        return Trip.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')

class TripDetailView(DetailView):
    model = Trip

    def get_context_data(self,**kwargs):
        context = super(TripDetailView, self).get_context_data(**kwargs)

        context['comments']= {}
        elements = Tripcomment.objects.all()

        print(len(elements))
        obj = get_object_or_404(Trip, id=self.kwargs['pk'])

        #user = get_object_or_404(AuthUser, pk=self.user.pk)

        for x in range (len(elements)):
            if elements[x].tripid.id == obj.id:
                context['comments'][x] = elements[x]
                #if context['comments'][x].bloggerid == user.id:

        return context

class CreateTripView(LoginRequiredMixin,CreateView):
    # I don't anyone to be able to access this CreateTripView
    # Mixins attributes
    # Specifies where the login url should be
    #template_name = 'blog_app/trip_form.html'
    login_url = '/login/'
    # redirect field :
    redirect_field_name = 'blog_app/trip_detail.html'

    form_class = TripForm

    model = Trip


    def form_valid(self,form):
        # This method is called when valid form data has been POSTED
        # It should return HttpResponse
        c_user = AuthUser.objects.get(id=self.request.user.id)
        form.instance.bloggerid = c_user
        return super(CreateTripView, self).form_valid(form)

class AddCommentToTrip(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/trip_detail.html'
    form_class = TripCommentForm
    model = Tripcomment

    def form_valid(self,form):
        c_user = AuthUser.objects.get(id=self.request.user.id)
        form.instance.bloggerid = c_user
        form.instance.date = timezone.localtime()
        c_trip = get_object_or_404(Trip,id=self.kwargs['pk'])
        form.instance.tripid = c_trip
        if c_user.id == c_trip.bloggerid.id:
            form.instance.approved = True
        else:
            form.instance.approved = False

        return super(AddCommentToTrip, self).form_valid(form)


class TripUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/trip_detail.html'
    form_class = TripForm
    model = Trip

class TripDeleteView(LoginRequiredMixin,DeleteView):
    model = Trip
    success_url = reverse_lazy('trip_list')

class DraftListView(LoginRequiredMixin,ListView):
    template_name = 'trip_draft_list.html'
    model = Trip

# make sure there is no publication date on it
    #def get_queryset(self):
    #    return Trip.objects.filter(publish_date__isnull=True).order_by('-date')

    def get_context_data(self,**kwargs):
        context = super(DraftListView, self).get_context_data(**kwargs)

        context['trips']= {}
        elements = Trip.objects.all()
        # context['c_users']= AuthUser.objects.all()
        c_user = AuthUser.objects.get(id=self.request.user.id)
        for x in range (len(elements)):
            if elements[x].bloggerid.id == c_user.id and elements[x].publish_date == None:
                context['trips'][x] = elements[x]

        return context
#############################################
#############################################
@login_required
def trip_publish(request,pk):
    obj = get_object_or_404(Trip,pk=pk)
    obj.publish_date = datetime.date.today()
    obj.save()
    return redirect('trip_draft_list')

class CommentUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/trip_detail.html'
    form_class = TripCommentForm
    model = Tripcomment

@login_required
def comment_approve(request,pk):
    com = get_object_or_404(Tripcomment,pk=pk)
    com.approved = True
    com.save()
    return redirect('trip_detail',pk=com.tripid.pk)

@login_required
def comment_remove(request,pk):
    com = get_object_or_404(Tripcomment,pk=pk)
    trip_pk = com.tripid.pk
    com.delete()
    return redirect('trip_detail',pk=trip_pk)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password1)
            user.save()
            c_user = user_form.instance.id
            profile = profile_form.save(commit=False)
            profile_form.instance.userid = AuthUser(c_user)
            profile.save()

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']

            profile.save()
            registered = True

        else:
            print(user_form.errors)
            print(profile_form.errors)

    else:
       user_form = UserForm
       profile_form = UserProfileForm

    return render(request,'registration/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

#def user_login(request):
 # request.user.get_profile().profilepic

 # if request.method == "POST":
#      username = request.POST.get('username')
#      password = request.POST.get('password')

#      user = authenticate(username=username,password1=password)
#      if user:
#          if user.is_active:
#              login(request,user)
#              return HttpResponseRedirect(reverse('trip_list'))
##          else:
#              return HttpResponse("ACCOUNT IS NOT ACTIVE!")
#      else:
#          print("Login credentials did not match")
#          print("Username: {} and Password: {}".format(username,password))
#          return HttpResponse("Please try again")

 # else:
#      return render(request,'registration/login.html',{})

@login_required
def edit_user(request, pk):
    c_user = AuthUser.objects.get(id=pk)
    c_profile = Userprofile.objects.get(id=c_user.userid.pk)

    if request.method == 'POST':
        user_form = UserForm(request.POST or None,instance = c_user)
        profile_form = UserProfileForm(request.POST or None, instance = request.c_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)

            if 'profilepic' in request.FILES:
                profile.profilepic = request.FILES['profilepic']

            profile.save()

        else:
            print(user_form.errors)
            print(profile_form.errors)

    else:
       user_form = UserForm
       profile_form = UserProfileForm

    return render(request,'blog_app/account_update.html',{'user_form':user_form,'profile_form':profile_form})

@login_required
def get_user_profile(request, pk):
    user = get_object_or_404(AuthUser, pk=pk)
    userprofiles = Userprofile.objects.all()
    profile = None
    for profile in userprofiles:
        if profile.userid.pk == user.id:
            profile = profile

        return render(request, 'blog_app/user_profile.html', {'user': request.user,'profile':profile})
