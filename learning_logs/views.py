from django.shortcuts import render
from .models import Topic 
# Create your views here.
def index(request):
    return render(request,"learning_logs\index.html")

def Topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,"learning_logs\Topic.html",context)
def topic(request,topic_id):
    top = Topic.objects.get(id = topic_id)
    entries = top.entry_set.order_by('date_added')
    context = {'topic':top,'entries':entries }
    return render(request,"learning_logs\detail.html",context)