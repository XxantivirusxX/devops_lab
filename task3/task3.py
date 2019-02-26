import psutil
import time
import configparser
import json


def crudConfig(path):
    config = configparser.ConfigParser()
    config.read(path)
    global output, interval
    output = config.get("config", "output")
    interval = config.get("config", "interval")
path = "config.ini"


crudConfig(path)


print(output)


def f():
    i = 0
    while True:
        i += 1
        a = str(i)
        cpout = str(psutil.cpu_percent(interval=1))
        vmout = str(psutil.virtual_memory())
        diskout = str(psutil.disk_usage('/'))
        ioout = str(psutil.net_io_counters(pernic=True))
        netout = str(psutil.net_connections())
        dat = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        if output == "txt":
            with open('OUT.txt', "a") as outfile:
                outfile.write(' '.join(('SNAPSHOT', a, ':', dat, cpout, '%', 
                    vmout, diskout, ioout, netout + '\n')))
                outfile.write("!!!!!" + '\n')
                outfile.close()
        elif output == "json":
            with open('OUT.json', 'a') as outfile:
                json.dump(('SNAPSHOT', a, dat, cpout, '%', vmout, diskout, 
                    ioout, netout), outfile)
                outfile.close()
        else:
            print("The wrong output format")
        time.sleep(int(interval))


f()
