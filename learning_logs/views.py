from django.shortcuts import render
from .models import Topic 
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import topicforms,entryforms
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

@login_required
def Topics(request):
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request,"learning_logs\Topic.html",context)

@login_required
def topic(request,topic_id):
    top = Topic.objects.get(id = topic_id)
    if (top.owner != request.user):
        raise Http404
    entries = top.entry_set.order_by('date_added')
    context = {'topic':top,'entries':entries }
    return render(request,"learning_logs\detail.html",context)

@login_required
def Newt(request):
    if(request.method != "POST"):
        form = topicforms()
    else:
        form = topicforms(request.POST)
        if form.is_valid():
            newt = form.save(commit=False)
            newt.owner = request.user
            newt.save()
            return HttpResponseRedirect(reverse('learning_logs:Topic'))
    context = {'form':form}
    return render(request,"learning_logs/newTopic.html", context)

@login_required
def Newe(request,topic_id):
    top = Topic.objects.get(id = topic_id)
    if(request.method != "POST"):
        eform = entryforms()
    else:
        eform = entryforms(data=request.POST)
        if eform.is_valid():
            new_entry = eform.save(commit = False)
            new_entry.topic = top
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:Topic',args = [topic_id]))
    context = {'topic':top,'form':eform}
    return render(request,'learning_logs/newEntry.html',context)