#!/usr/bin/python3

import requests
import argparse
from bs4 import BeautifulSoup

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('URL', help='URL to query')
    args = parser.parse_args()

    response = requests.get(args.URL)
    b = BeautifulSoup(response.content.decode("UTF-8"))
    el = b.find(id="visitorcount-container")
    count = el.get("data-value")
    postr = requests.post('http://localhost:8086/write?db=collectd',
                        data="bouldern,ident=zirndorf {}".format(count))
    print(postr.status)
    sys.exit(0)
    
