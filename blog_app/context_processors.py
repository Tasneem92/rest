from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from blog_app.models import Trip,AuthUser,Tripcomment,Vote,Userprofile
from django.contrib.auth.models import User
from blog_app.forms import TripForm, StoryForm, UserForm,TripCommentForm,UserProfileForm
from django.urls import reverse_lazy # it waits until I delete the trip until it view the url
from django.contrib.auth import authenticate, login, logout
# zay el decorator ta3 el functions based view bas lal classes based view
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.core.urlresolvers import reverse
import datetime
from django.shortcuts import render_to_response
from django.template import RequestContext

def get_profile(request):
    if request.user.is_authenticated():
        user = AuthUser.objects.get(id=request.user.id)
        userprofiles = Userprofile.objects.all()
        pro = 0
        profile = None
        for profile in userprofiles:
            if profile.userid.pk == user.id:
                pro = profile.profileid
                profile = profile
                return {'user': request.user,'profile':profile}
        return {'user': request.user}
    else:
        return {}
