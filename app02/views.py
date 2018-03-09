from django.shortcuts import render,HttpResponse,Http404
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.utils.decorators import method_decorator
from django.views.generic import View
from utils.permissions_mixin import CustomLoginRequiredMixin,CustomPermissionRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin




class IndexView(CustomPermissionRequiredMixin,View):
    get_permission = ['app02.reply_discussion','app02.reply_discussion2']
    post_permission = ['app02.create_discussion','app02.create_discussion2']
    # # get_permission = ['app02.reply_discussion2',]
    # post_permission = ['app02.create_discussion2',]




    def get(self,request):
        return render(request,'index.html')


    def post(self,request):
        return HttpResponse("post")


