from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import simplejson as json
from simplejson.compat import StringIO
from datetime import datetime, date, time

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from django.contrib.syndication.views import Feed

from django.views.generic.edit import CreateView

from .defReadDB import *




# Create your views here.


#------------------------------------------------------------------
def logout_view(request):

    logout(request)

    # Redirect to a success page.

    return redirect('/')


#------------------------------------------------------------------
@login_required(login_url='/accounts/login/')

def pageone(request):
    #print('pageone')
    #---------------
    user = str(request.user)

    context_dict = {}
    #---------------
    # посты пользователя
    (error_post, qpost) = readUserPost(user)

    # посты подписанных пользователей
    (error_signpost, qsignpost) = receiveSignPost(user)

    #------------
    context_dict['user'] = user
    context_dict['qpost'] = qpost
    context_dict['qsignpost'] = qsignpost
    
    
    return render(
                request, 
                'blog/pageone.html', 
                context_dict
                ) 

#------------------------------------------------------------------
def pagetwo(request, idn):
    #print('pagetwo')
    #---------------
    user = str(request.user)

    context_dict = {}
    #---------------
    # посты пользователя
    (error_post, qpost) = getPost(idn)

    #------------
    context_dict['user'] = user
    context_dict['post'] = qpost
    
    return render(
                request, 
                'blog/pagetwo.html', 
                context_dict
                ) 

#------------------------------------------------------------------
def postwrite(request, idn):
    # idn - id прочитанного пользователем поста
    #print('postwrite')
    #---------------
    user = str(request.user)

    error = writeReadPost(user, idn)

    # переходим на первую страницу
    return redirect('/')
 

#------------------------------------------------------------------
class BlogPostAdd(CreateView):
    
    model = BlogPost
    fields = ['user', 'header', 'content', ]
    success_url = '/'
    
    def get_initial(self):
        return { 'user': self.request.user }





