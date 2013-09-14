import argparse
import pycurl
import StringIO
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
    
'''
Created on 13.09.2013

"http://%s:%d/testsite?query=STATUSFILEAGETT,NUMHSTUP"
@author: Marco Hoyer
'''
    
def get_by_http(targethost, port, uri, params):
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, "http://%s:%d%s?%s" % (targethost,port, uri, params))
    curl.setopt(pycurl.CONNECTTIMEOUT, 10)
    
    contents = StringIO.StringIO()
    curl.setopt(pycurl.WRITEFUNCTION, contents.write)
    try:
        curl.perform()
    except:
        print "Error: could not get data via http"
        return None

    if curl.getinfo(pycurl.HTTP_CODE) == 200:
        return contents.getvalue()
    else:
        print "Error: Targethost responded with HTTP-" + str(curl.getinfo(pycurl.HTTP_CODE))
        return None

# main action
def main(args):
    print get_by_http("localhost",80,"/testsite","query=STATUSFILEAGETT,NUMHSTUP")
    

# parameter handling separation
if __name__ == '__main__':
    # parameter handling
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="show debug output", action="store_true")
    parser.add_argument("--verbose", help="show verbose output", action="store_true")
    parser.add_argument("hostname", help="hostname", type=str)
    parser.add_argument("port", help="port",type=str)
    parser.add_argument("url", help="url for resource to query", type=str)
    parser.add_argument("key", help="key to query for", type=str)
    args = parser.parse_args()
    main(args)