import _thread
from subprocess import Popen,PIPE
import time
find_ip=[]
def ping_check(ip):
    listone=[]
    global find_ip
    try:
        check=Popen("ping -c1 {} 2>/dev/null".format(ip),stdout=PIPE,shell=True)
        data=check.stdout.read().decode('utf8')
        if 'from' in data:
            print(ip)
            find_ip.append(ip)
    except Exception as error:
        pass
    finally:
        pass
    return find_ip


def start_findip():
    ips=[]
    for i in range(137,141):
        if i != 138:
            ip='192.168.86.'+str(i)
            ips=_thread.start_new_thread(ping_check,(ip,))
            time.sleep(0.5)
    return ips
# main()
# start_findip()