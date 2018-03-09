from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render,HttpResponse,Http404


class CustomLoginRequiredMixin(LoginRequiredMixin):
    get_permission = []
    post_permission = []


class CustomPermissionRequiredMixin(object):
    get_permission = []
    post_permission = []


    def dispatch(self, request, *args, **kwargs):


        if request.method == 'GET':
            if self.get_permission:
                if  self.request.user.has_perms(self.get_permission):
                    return super(CustomPermissionRequiredMixin, self).dispatch(
                            request, *args, **kwargs)
                else:
                    return render(request, "403.html")
            else:

                return render(request, "403.html")



        elif request.method == 'POST':
            if self.post_permission:
                if  self.request.user.has_perms(self.post_permission):
                    return super(CustomPermissionRequiredMixin, self).dispatch(
                            request, *args, **kwargs)
                else:
                    return render(request, "403.html")
            else:

                return render(request, "403.html")