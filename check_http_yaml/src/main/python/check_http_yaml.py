import argparse
import requests
import sys
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
    
def exit_ok(message):
    print "OK - " + message
    sys.exit(0)
    
def exit_warning(message):
    print "WARNING - " + message
    sys.exit(1)
    
def exit_critical(message):
    print "CRITICAL - " + message
    sys.exit(2)
        
def exit_unknown(message):
    print "UNKNOWN - " + message
    sys.exit(3)
    
def construct_url(targethost, port, uri, params):
    return "http://%s:%d%s?%s" % (targethost,port, uri, params)
    
def get_by_http(url):
    try:
        response = requests.get(url)
    except Exception as e:
        exit_unknown(repr(e))
    if (response.status_code == 200):
        return response.text
    else:
        exit_unknown("server responded with status-code " + str(response.status_code))
        return None
    
def check_value(value, warning, critical, inverse):
    if inverse:
        if (value > warning):
            exit_ok("")
        elif (value > critical):
            exit_warning("")
        else:
            exit_critical("")
    else:
        if (value < warning):
            exit_ok("")
        elif (value < critical):
            exit_warning("")
        else:
            exit_critical("")
        
def check_tresholds(warning, critical, inverse):
    if (warning == critical):
        exit_unknown("warning and critical cannot be equal")
    if inverse:
        if (warning <= critical):
            exit_unknown("warning must be bigger than critical")
    else:
        if (warning >= critical):
            exit_unknown("warning must be lower than critical")

# main action
def main(args):
    print get_by_http( construct_url("localhost",80,"/testsite","query=STATUSFILEAGETT") )
    

# parameter handling separation
if __name__ == '__main__':
    # parameter handling
    parser = argparse.ArgumentParser(description='Checks for values in a key-value yaml dict offered by http')
    parser.add_argument("--debug", help="show debug output", action="store_true")
    parser.add_argument("--warning", help="warning thresholds", type=int)
    parser.add_argument("--critical", help="critical thresholds", type=int)
    parser.add_argument("--inverse", help="invert thresholds", action="store_true")
    parser.add_argument("--perfdata", help="print perfdata values", action="store_true")
    parser.add_argument("--hostname", help="hostname", type=str)
    parser.add_argument("--port", help="port",type=int)
    parser.add_argument("--url", help="url for resource to query", type=str)
    parser.add_argument("--key", help="key to query a value for", type=str)
    args = parser.parse_args()
    main(args)