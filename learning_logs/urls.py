from django.urls import path
from . import views

app_name = 'learning_logs'

urlpatterns = [path(r'',views.index,name = 'index'),
               path(r'Topics',views.Topics,name = 'Topic'),
               path(r'Topics/(?P<topic_id>\d+)/',views.topic,name = 'Topic'),
               path(r'^New_Topic/$',views.Newt,name = "New_Topic"),
               path(r'New_entry/(?P<topic_id>\d+)',views.Newe,name = 'New_Entry')]

# urlpatterns = []
# urlpatterns = [re_path(r'^topic/$',views.topic,name = 'topic')]