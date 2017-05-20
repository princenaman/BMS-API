#!/usr/bin/python

import re
import urllib2
import sys

class BookMyShowClient(object):

  def __init__(self):
    code = sys.argv[1]
    text = sys.argv[2]
    self.__cookie = "Rgn=|Code=%s|text=%s|" % (code , text)
    self.__url = "https://in.bookmyshow.com/serv/getData?cmd=QUICKBOOK&type=MT"

  def get_json(self):
    req = urllib2.Request(self.__url, headers={'User-Agent' : "Magic Browser"})
    req.add_header('Cookie', (self.__cookie))
    html = urllib2.urlopen(req).read()
    return html

if __name__ == '__main__':
  bms_client = BookMyShowClient()
  json = bms_client.get_json()
  print json
