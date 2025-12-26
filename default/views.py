from django.shortcuts import render
from .models import poll, Option
from django.views. generic import ListView, DetailView, RedirectView,CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req, "default/list.html", {'poll_list': polls, 'msg': 'Hello!'})

class PollList(ListView):
    model = poll
     
     #應用程式名稱/資料模型_list.html
     #defult/poll_list.html

class PollView(LoginRequiredMixin, DetailView):
    model = poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        option_list =Option.objects.filter(poll_id=self.object.id)
        ctx['option_list'] = option_list
        return ctx

class pollvote(LoginRequiredMixin, RedirectView):
    #redirect_url = "http://ww.google.com/"

    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id = self.kwargs['oid'])
        option.vote +=1
        option.save()
        #return  "/poll/{}/".format(option.poll_id)
        return reverse('poll_view', kwargs={'pk': option.poll_id})
        
class PollCreate(LoginRequiredMixin, CreateView):
    model= poll
    fields = '__all__' #['subject, 'desc']
    success_url = reverse_lazy('poll_list')
class PollEdit(UpdateView):
    model= poll
    fields = '__all__' #['subject, 'desc']

    def get_success_url(self):
        return reverse_lazy('poll_view', kwargs={'pk':self.object.id})

class OptionCreate(LoginRequiredMixin, CreateView):
    model = Option
    fields = ['title']

    def form_valid(self, form):
        form.instance.poll_id =self.kwargs['pid']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('poll_view', kwargs={'pk':self.kwargs['pid']})

class OptionEdit(LoginRequiredMixin, UpdateView):
    model = Option
    fields = ['title']
    pk_url_kwarg = 'oid'

    def get_success_url(self):
        return reverse_lazy('poll_view', kwargs={'pk':self.object.poll_id})

class PollDelete(LoginRequiredMixin, DeleteView):
    model = poll
    success_url = reverse_lazy('poll_list')
class OptionDelete(LoginRequiredMixin, DeleteView):
    model = Option

    def get_success_url(self):
        return reverse_lazy('poll_view', kwargs={'pk':self.object.poll_id})