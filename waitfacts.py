from multiprocessing.pool import ThreadPool
import requests
import time

def waitfacts(num_seconds=5):
    def waitfacts_(f):
        def inner(*args):
            pool = ThreadPool(processes=2)
            t = pool.apply_async(f, args)
            while not t.ready():
                time.sleep(num_seconds)
                print get_fact() + "\n"
            print "\n"
        return inner
    return waitfacts_
 
def get_fact():
    """ Gets a fact from mentalfloss's fun facts API. """
    
    url = "http://mentalfloss.com/api/1.0/views/amazing_facts.json?limit=1"
    r = requests.get(url)
    try:
        raw = r.json()[0]['nid']
    except NoneType:
        return get_fact()

    return raw[3:-5]
