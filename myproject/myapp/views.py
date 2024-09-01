from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import IPAddress
from .forms import IPAddressForm
from django.urls import reverse_lazy
from myapp import tasks
from .models import IPAddress, PingResult
from django.http import JsonResponse
from django.utils import timezone

# Create your views here.

def indexview(request):
    return render(request,'index.html')

class IPListView(ListView):
    model = IPAddress
    template_name = 'listipaddress.html'
    context_object_name = 'iplist'

class IPCreateView(CreateView):
    model = IPAddress
    form_class = IPAddressForm
    template_name = 'ip_address_form.html'
    success_url = reverse_lazy('myapp:iplistview')

def monitorstartview(request):
    print("Monitor Starting")
    allip = IPAddress.objects.all()
    for ip in allip:
        tasks.startscheduler(str(ip))
    return render(request,'startmonitor.html')

def enablemonitorview(request):
    return render(request,'enablemonitor.html')

def plotgraph(request, pk=1):
    print("get latency called***************************************")
    print(pk)
    # Get data from the last 24 hours (for example)
    #start_time = timezone.now() - timezone.timedelta(days=1)
    #records = PingResult.objects.filter(timestamp__gte=start_time,address_id=pk).order_by('timestamp')
    records = PingResult.objects.filter(address_id=pk).order_by('timestamp')[:10]

    # Prepare data for JSON response
    timestamps = [record.timestamp.isoformat() for record in records]
    latencies = [record.response_time for record in records]

    print(timestamps)
    data = {
        'timestamps': timestamps,
        'latencies': latencies
    }

    return JsonResponse(data)

def graph(request, pk):
    mydic = {'pk':pk}
    return render(request,'chart.html',mydic)
