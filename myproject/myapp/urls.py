from django.urls import path
from . import views


app_name = 'myapp'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.indexview,name='indexview'),
    path('iplist/',views.IPListView.as_view(),name='iplistview'),
    path('ipcreate/',views.IPCreateView.as_view(),name='ipcreateview'),
    path('enablemonitor/',views.enablemonitorview,name='enablemonitorview'),
    path('monitorstart/',views.monitorstartview,name='monitorstartview'),
    path('graph/<int:pk>/',views.graph,name='graph'),
    path('graph/<int:pk>/graph',views.plotgraph,name='plotgraph'),

]
