from django.shortcuts import render
from .models import poll, Option
from django.views. generic import ListView, DetailView, RedirectView
from django.urls import reverse
# Create your views here.
def poll_list(req):
    polls = poll.objects.all()
    return render(req, "default/list.html", {'poll_list': polls, 'msg': 'Hello!'})

class PollList(ListView):
    model = poll
     
     #應用程式名稱/資料模型_list.html
     #defult/poll_list.html

class PollView(DetailView):
    model = poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        option_list =Option.objects.filter(poll_id=self.object.id)
        ctx['option_list'] = option_list
        return ctx

class pollvote(RedirectView):
    #redirect_url = "http://ww.google.com/"

    def get_redirect_url(self, *args, **kwargs):
        option = Option.objects.get(id = self.kwargs['pk'])
        option.vote +=1
        option.save()
        #return  "/poll/{}/".format(option.poll_id)
        return reverse('poll_view', args=[option.poll_id])
        
