#!/usr/bin/env python2.7
# script by Alex Eames http://RasPi.tv/?p=7684
# http://RasPi.tv/
import time
from subprocess import call
from threading import Thread

cmd = "python /home/pi/presort.py"  # customise this command

def process_thread(i):
    print "Thread: %d" % i
    start_time = time.time()
    call ([cmd], shell=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print "Thread %s took %.2f seconds" % (i, elapsed_time)

how_many = int(raw_input("How many threads?\n>"))

for i in range(how_many):
    t = Thread(target=process_thread, args=(i,))
    t.start()