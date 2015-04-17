from multiprocessing.pool import ThreadPool
import json
import requests
import time
import sys

def waitfacts(f):
    def inner():
        pool = ThreadPool(processes=2)
        t = pool.apply_async(func=f)
        while not t.ready():
            time.sleep(2)
            print get_fact() + "\n"
        print "\n"
    return inner

def get_fact():
    """ Gets a fact from mentalfloss's fun facts API. """

    url = "http://mentalfloss.com/api/1.0/views/amazing_facts.json?limit=1"
    r = requests.get(url)
    raw = r.json()[0]['nid']
    return raw[3:-5]
