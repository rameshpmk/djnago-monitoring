import time
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from .models import IPAddress, PingResult
from ping3 import ping
from scapy.all import sr1, ICMP, IP

def pingstart(address):
    #print(type(address))
    print("BackgroundScheduler Executing...")
    print(address)

    response_time = ping(address, timeout=10)
    if isinstance(response_time, (int,float)):
        response_time = response_time * 1000
    #time.sleep(2)
    print(response_time)

    if response_time == False or response_time == None:
        status = "unreachable"
        color = "red"
    else:
        status = "reachable"
        color = "green"
    print(status)

    object = IPAddress.objects.get(address=address)
    time.sleep(5)

    if address:
        PingResult.objects.create(address = object, response_time=response_time,status=status)
    print("Create Success")



def startscheduler(address):
    print("Entering in startscheduler")
    scheduler = BackgroundScheduler()
    scheduler.add_job(pingstart, 'interval', seconds = 10, args=[address])
    scheduler.start()
    return
