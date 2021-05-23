#!/usr/bin/python3

import sys
import os
import requests
import argparse
from bs4 import BeautifulSoup

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('URL', help='URL to query')
    parser.add_argument('LOCATION', help='URL to query')
    args = parser.parse_args()

    response = requests.get(args.URL)
    b = BeautifulSoup(response.content.decode("UTF-8"), "html.parser")
    el = b.find(id="visitorcount-container")
    count = el.get("data-value")
    #os.system("curl http://localhost:8086/write?db=collectd \
    #                -XPOST --data-binary 'bouldern,ident=zirndorf value={}'".format(count))
    postr = requests.post('http://localhost:8086/write?db=collectd',
                        data="bouldern,ident={} value={}".format(args.LOCATION, count),
                        headers={'Content-Type': 'application/octet-stream'})
    sys.exit(0)
    

